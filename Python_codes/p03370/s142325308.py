n,x = map(int,input().split())
m = [int(input()) for i in range(n)]

sum_m = sum(m)
remain = x - sum_m
min_m = min(m)
cnt = remain // min_m

print(n+cnt)