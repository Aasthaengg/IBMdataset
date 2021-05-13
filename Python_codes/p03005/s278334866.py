N,K=map(int, input().split())

if K == 1:
  out =0
else:
  # 1以外
  nokori = N - K
  mx = nokori + 1
  mn = 1
  out = mx-mn

print(out)
