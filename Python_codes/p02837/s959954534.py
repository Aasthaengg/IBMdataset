n=int(input())
s=[]
ans=0
for i in range(n):
    a=int(input())
    s.append([list(map(int,input().split())) for _ in range(a)])
for i in range(2**n):
    bit=bin(i)[2:].zfill(n)
    flag=1
    for j in range(n):
        if bit[j]=='0':
            continue
        for sh in s[j]:
            if int(bit[sh[0]-1])!=sh[1]:
                flag=0
    if flag:
        ans=max(ans,bit.count('1'))
print(ans)