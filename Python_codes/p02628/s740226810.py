N, K = map(int,input().split())
P = list(map(int,input().split()))
P_sorted = sorted(P)
sum_ = 0
i = 0
while K>0:
    sum_ = sum_+P_sorted[i]
    K=K-1
    i = i+1
print(sum_)