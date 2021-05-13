N = int(input())
A = list(map(int, input().split()))
ans = 1
for i in A:
  if i == ans:
    ans += 1
print("-1" if ans == 1 else len(A)-ans+1)