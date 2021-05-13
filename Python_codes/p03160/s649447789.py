n=int(input())
arr=list(map(int,input().split()))
if n < 2:
  print(0)
vis = [0] * n
vis[0] = 0
vis[1] = abs(arr[0]-arr[1])
for i in range(2, n):
    step_1 = abs(arr[i]-arr[i-1]) + vis[i-1]
    step_2 = abs(arr[i]-arr[i-2]) + vis[i-2]
    vis[i] = min(step_1, step_2)
print(vis[-1])