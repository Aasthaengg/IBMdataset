N, K = map(int, input().split())
X = list(map(int, input().split()))

lis = []
for i in range(N-K+1):
    left = X[i]
    right = X[i+K-1]
    res = right - left
    abs_l, abs_r = abs(left), abs(right)
    if abs_l > abs_r: 
       res += abs_r
    else:
       res += abs_l
    lis.append(res)
print(min(lis))
