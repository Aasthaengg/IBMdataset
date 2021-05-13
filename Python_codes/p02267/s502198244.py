n=int(input())
S=list(map(int,input().split()))

q=int(input())
T=list(map(int,input().split()))
c=0
for i in T:
    for j in S:
        if i==j:
            c+=1
            break
print(c)