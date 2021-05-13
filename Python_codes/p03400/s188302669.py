N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]
ans = X
for x in A:
  ans += (D-1)//x+1
print(ans)