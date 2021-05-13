N=int(input())
p=[int(input()) for i in range(N)]

max_p = max(p)
sum_p = sum(p)-max_p//2
print(sum_p)