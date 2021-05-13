n,m=map(int,input().split())
s=[]
for i in range(n):
    a1,b1=map(int,input().split())
    s.append([a1,b1])
s.sort()
k=0
h=0
for i in range(n):
    h+=s[i][1]
    k+=s[i][0]*s[i][1]
    if h>=m:
        k-=(h-m)*s[i][0]
        break
print(k)