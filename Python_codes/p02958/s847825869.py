n = int(input())
p = list(map(int,input().split()))
x = sorted(p)
c = 0
for i in range(n):
    if p[i]!=x[i]:
        c += 1
if c<=2:
    print("YES")
else:
    print("NO") 