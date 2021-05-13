# B - Card Game for Two
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
for i in range(N):
    ans = ans+A[i] if i%2==0 else ans-A[i]
print(ans)