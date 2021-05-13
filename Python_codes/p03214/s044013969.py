N = int(input())
A = [int(x) for x in input().split()]
mean_a = sum(A)/N
ans = 0
ans_dist = float('inf')
for ind,a in enumerate(A):
    if(abs(mean_a-a)<ans_dist):
        ans_dist = abs(mean_a-a)
        ans = ind
print(ans)
