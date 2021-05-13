o = list(input())
e = list(input())
ans = []

if len(o) != len(e):
    e += [""]

for i in range(len(o)):
    ans += [o[i],e[i]]
print(*ans,sep="")