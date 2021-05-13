N = int(input())
H = list(map(int, input().split()))

memo = [0]*N

for i in range(1,N):
    if H[i-1]>=H[i]:
        memo[i] = memo[i-1]+1
    else:
        memo[i] = 0
        
print(max(memo))