from sys import stdin
def i():
    return stdin.readline().rstrip()
def mi():
    return map(int(),stdin.readline().rstrip().split())
def li():
    return list(map(int,stdin.readline().rstrip()))
ans=10000
s=i()
t=i()
ls=len(s)
lt=len(t)
l=ls-lt
for i in range(l+1):
    cnt=0
    for j in range(lt):
        if s[i+j]!=t[j]:
            cnt+=1
    if cnt<ans:
        ans=cnt

print(ans)