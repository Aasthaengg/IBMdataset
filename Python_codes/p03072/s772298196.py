N=int(input())
H=list(map(int,input().split()))
a=1
for i in range(1,N):
    if H[i]>=max(H[0:i]):
        a+=1
print(a)