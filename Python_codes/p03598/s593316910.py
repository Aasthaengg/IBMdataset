N=int(input())
K=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(N):
    if l[i]<K-l[i]:
        sum+=2*l[i]
    else:
        sum+=2*(K-l[i])
print(sum)
