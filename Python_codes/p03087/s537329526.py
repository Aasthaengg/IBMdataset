n,q=map(int,input().split())
s=input()

ac=[0]*n
for i in range(n-1):
    ac[i+1]=ac[i]
    if s[i]=="A" and s[i+1]=="C":
        ac[i+1]+=1


lr=[]
for i in range(q):
    lr.append(list(map(int,input().split())))

for i in range(q):
    print(ac[lr[i][1]-1]-ac[lr[i][0]-1])
