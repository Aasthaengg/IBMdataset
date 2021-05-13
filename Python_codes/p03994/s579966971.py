s = input()
n = len(s)
c = [ord(s[i]) for i in range(n)]
k = int(input())
ind = 0
while k > 0:
    if ind == n:
        break
    if c[ind] == 97:
        ind += 1
        continue
    elif 123 - c[ind] <= k:
        k -= 123-c[ind]
        c[ind] = 97
        ind += 1
    elif 123 - c[ind] > k:
        ind += 1
        continue

if k > 0:
    k %= 26
    c[-1] += k
    if c[-1] >= 123:
        c[-1] = 97 + (123-c[-1])

print(''.join([chr(c[i]) for i in range(n)]))