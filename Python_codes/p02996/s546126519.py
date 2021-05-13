n = int(input())
a = []
b = []
for i in range(n):
    p,q = map(int,input().split())
    a.append(p)
    b.append(q)

ab = zip(b,a)
ab = sorted(ab)
b,a = zip(*ab)

val = 0
ans  = "Yes"
for i in range(n):
    val +=a[i]
    if val > b[i]:
        ans = "No"
        break
print(ans)