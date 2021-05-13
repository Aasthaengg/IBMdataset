from bisect import bisect_left
x=input()
s,t=[],[]
n=len(x)
for i in range(n):
    if x[i]=="S":
        s.append(i)
    else:
        t.append(i)
ans,cnt=0,0
#print(t)
for idx in t:
    if bisect_left(s,idx)-cnt>0:
        ans+=1
        cnt+=1
print(n-2*ans)