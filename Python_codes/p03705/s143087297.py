n,a,b = map(int,input().split())

min_sum = 0

min_sum = a*(n-1) + b
max_sum = b*(n-1) + a

print(max(0,max_sum-min_sum+1))