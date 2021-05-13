N, = list(map(int,input().split()))
K, = list(map(int,input().split()))
x  = list(map(int,input().split()))
print(sum([2*min(x[i],abs(x[i]-K)) for i in range(N)]))