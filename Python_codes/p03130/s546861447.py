c=[0 for i in range(4)]
for i in range(3):
    a,b=list(map(int,input().split()))
    c[a-1]+=1;c[b-1]+=1
print("YES" if c.count(2)==2 and c.count(1)==2 else "NO")