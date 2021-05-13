n,k=map(int,input().split())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])
abc=sorted(ab,key=lambda x:x[0])
temp=0
for j in abc:
    temp+=j[1]
    if temp>=k:
        print(j[0])
        exit()