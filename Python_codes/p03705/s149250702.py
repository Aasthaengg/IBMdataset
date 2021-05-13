n,Min,Max = map(int,input().split())
sum_min = Min * (n-1) + Max
sum_max = Max * (n-1) + Min
ans = sum_max - sum_min + 1
print(max(0,ans))
