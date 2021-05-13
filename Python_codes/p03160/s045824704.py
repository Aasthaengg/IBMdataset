N = int(input())
h = list(map(int,input().split()))
ans = [0]*N
ans[1] = abs(h[1] - h[0])
for i in range(N - 2):
  p1 = ans[i] + abs(h[i] - h[i + 2])
  p2 = ans[i + 1] + abs(h[i+1] - h[i+2])
  ans[i + 2] = min([p1,p2])
print(ans[N-1])  