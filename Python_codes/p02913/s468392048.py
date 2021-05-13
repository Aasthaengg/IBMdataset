n = int(input())
s = input()

mod = 10**20 + 7
base = 12345

def ok(l):
    array = {}
    rolling_hash = 0
    for i in range(n):
        rolling_hash *= base
        rolling_hash += ord(s[i])
        if i - l >= 0:
            rolling_hash -= ord(s[i-l]) * pow(base, l, mod)
        rolling_hash %= mod
        if i >= l-1:
            if rolling_hash in array.keys():
                array[rolling_hash].append(i)
            else:
                array[rolling_hash] = [i]
    for check in array.values():
        if max(check) - min(check) >= l:
            return True
    return False

top = n
bottom = 0

while top - bottom > 1:
    mid = (top + bottom)//2
    if ok(mid):
        bottom = mid
    else:
        top = mid
print(bottom)
