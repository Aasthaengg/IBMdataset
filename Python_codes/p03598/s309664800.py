N=int(input())
K=int(input())
x=list(map(int, input().split()))
print(sum([min(x[i], abs(x[i]-K)) for i in range(N)])*2)