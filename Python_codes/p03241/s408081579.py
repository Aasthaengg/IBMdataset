n,m=map(int,input().split())
#mの約数を調べる
temp=[]
i=1
while i*i<=m:
    if m%i==0:
        temp.append(i)
        if m//i!=i:
            temp.append(m//i)
    i+=1
temp.sort()
for i in temp:
    if i>=n:
        print(m//i)
        break