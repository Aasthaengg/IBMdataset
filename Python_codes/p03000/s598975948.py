N,X = map(int,input().split())
l=[0]
l += list(map(int,input().split()))
sum=0
for i in range(N+1):
    sum += l[i]
    if sum>X:
        print(i)
        exit()
print(N+1)
