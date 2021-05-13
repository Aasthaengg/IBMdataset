n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
ans = 0
for aa in a:
    tmp = 0
    for bbb,aaa in zip(b,aa):
        tmp += bbb*aaa
    tmp += c
    if tmp > 0:
        ans += 1
print(ans)
