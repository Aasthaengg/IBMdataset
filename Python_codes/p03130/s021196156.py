s=[0]*5
for i in range(3):
    a,b=map(int,input().split())
    s[a]+=1
    s[b]+=1

if s.count(2)==2:
    print("YES")
else:
    print("NO")
