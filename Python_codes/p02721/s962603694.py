import sys
n,k,c=map(int, input().split())
s=str(input())

l=[0]*n
r=[0]*n
i=0
j=n-1
cnt=0
while i<n:
    if s[i]=='x':
        i+=1
    if s[i]=='o':
        l[i]=1
        i+=c+1
        cnt+=1
#前から働いていって、必要以上の数働ける形の場合、必須となる日はありません。
if cnt>k:
    sys.exit()
    
while j>=0:
    if s[j]=='x':
        j-=1
    if s[j]=='o':
        r[j]=1
        j-=c+1
"""
ここまでで、lには「最速でその日に仕事ができる」
rには「遅くともその日までには仕事しないといけない」
というリストができます。

print(l)
print(r)
"""
for _ in range(len(l)):
    if l[_] and r[_]:
        print(_+1)