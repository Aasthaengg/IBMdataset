n=int(input())
b=[bin(int(i))[2:] for i in input().split()]
ind=0
i=0
l=[0]*20
ans=0
tmp=0
for i in range(n):
    if i>0 and ind<n:
        for j in range(len(b[i-1]))[::-1]:
            if b[i-1][j]=="1":
                l[j-len(b[i-1])]-=1
        for j in range(len(b[ind]))[::-1]:
            if b[ind][j]=="1":
                l[j-len(b[ind])]-=1
    ans+=ind-i
    while ind<n:
        for j in range(len(b[ind]))[::-1]:
            if b[ind][j]=="1":
                l[j-len(b[ind])]+=1
        if 2 in l:
            break
        else:
            ind+=1
            ans+=1
print(ans)

    








