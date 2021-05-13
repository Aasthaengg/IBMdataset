n = int(input())
d=[]
b=[]
cnt=0
for i in range(n):
    a = int(input())
    d.append(a)
for i in range(101):
    b.append(0)
for i in d:
    if b[i]==0:
        b[i]=i
        cnt+=1

print(cnt)