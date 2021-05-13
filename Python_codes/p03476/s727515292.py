def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def bisect(lst, isok, ok, ng):
    while(abs(ok-ng)>1):
        mid = (ok+ng)//2
        if isok(lst[mid]):
            ok = mid
        else:
            ng = mid
    return ok

s = []
for i in range(10**5):
    if i%2 == 1 and is_prime(i) and is_prime((i+1)//2):
        s.append(i)

s.sort()

q = int(input())
for k in range(q):
    l, r = map(int, input().split())
    l0 = bisect(s, lambda x:x >= l, len(s), -1)
    r0 = bisect(s, lambda x:x <= r, -1, len(s))
    print(max(0, r0-l0+1))