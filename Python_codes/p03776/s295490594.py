kai = [1]

s = 1
for i in range(1,51):
    s *= i
    kai.append(s)

n,a,b = map(int,input().split())

vl = list(map(int,input().split()))
vl = sorted(vl)
member = vl[-a:]
ans = sum(vl[-a:]) / len(vl[-a:])
v = vl[-a]
m = vl.count(v)
k = member.count(v)
if member[0] == member[-1]:
    print(ans)
    ans2 = 0
    for i in range(a, min(b, m)+1):
        ans2 += kai[m] // (kai[i] * kai[m-i])
    print(ans2)

else:
    print(ans)
    print(kai[m]//(kai[k] * kai[m-k]))
