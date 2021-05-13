N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ans = 1
num_color = [-1, -1, -1]
for a in A:
  ans = (ans * num_color.count(a-1)) % MOD
  try:
    num_color[num_color.index(a-1)] = a
  except:
    print(0)
    quit()

print(ans)