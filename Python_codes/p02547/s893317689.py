N = int(input())
flag = 0
ans = "No"

for i in range(N):
  tmp1, tmp2 = list(map(int, input().split()))
  if tmp1 - tmp2 == 0:
    flag += 1
  else:
    flag = 0
  if ans == "Yes" or flag >= 3:
    ans = "Yes"
print(ans)