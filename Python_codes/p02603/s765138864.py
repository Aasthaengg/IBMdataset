N=int(input())
A=list(map(int,input().split()))
money=1000
buy=0
for i in range(N-1):
    if A[i]<=A[i+1]:
        buy=money//A[i]
        money=A[i+1]*buy+money%A[i]
print(money)