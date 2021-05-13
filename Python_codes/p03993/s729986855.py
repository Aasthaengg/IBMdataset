N = int(input())
s = list(map(int ,input().split()))
con = 0
for i in range(N):
  if s[s[i] - 1] == i + 1:
    con += 1
print(con // 2)