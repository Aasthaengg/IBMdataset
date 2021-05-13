n,k = map(int, input().split())
b = list(map(int, input().split()))
a=0
for i in range(n):
    b[i] -= 1
if k<n:
    for i in range(k):
        a = b[a]
    print(a+1)
    exit()
c = [-1]*n
cc = 0
se = set()
while a not in se:
    c[a] = cc
    cc += 1
    se.add(a)
    a = b[a]
for i in range((k-c[a])%(cc-c[a])):
    a = b[a]
print(a+1)