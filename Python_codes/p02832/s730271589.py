n = int(input())
A = list(map(int, input().split()))

f=0
for a in A:
    if a==f+1:
        f+=1

if f==0:
    print(-1)
else:
    print(n-f)