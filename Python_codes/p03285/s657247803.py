N = int(input())

ans = "No"

for four in range(N//4 + 1):
  if (N - four * 4)%7 == 0:
    ans = "Yes"
    break
print(ans)