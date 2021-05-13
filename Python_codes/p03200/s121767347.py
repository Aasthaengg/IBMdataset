s=list(input())
ls=len(s)
ans=0
wpoint=[i for i, v in enumerate(s) if v=="W"]
wnum=len(wpoint)

for i in range(wnum):
    ans+=wpoint[i]-i
print(ans)