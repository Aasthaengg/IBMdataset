b, c = map(str, input().split())
d = b+c
for n in range(int(d)):
    if n == 0:
        continue
    if ((int(d)/n) == n):
        print('Yes')
        break
    if (n+1) == int(d):
        print('No')