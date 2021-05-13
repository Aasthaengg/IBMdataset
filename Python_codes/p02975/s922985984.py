from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
s = list(set(a))
l = len(s)

if l == 1 and a[0] == 0:
    print('Yes')
    exit()
if len(a) % 3 == 0:
    if l == 2 and c[0] == n // 3:
        print('Yes')
        exit()
    if l == 3 and s[0] ^ s[1] ^ s[2] == 0:
        tmp = n//3
        if all(x == tmp for x in c.values()):
            print('Yes')
            exit()

print('No')
