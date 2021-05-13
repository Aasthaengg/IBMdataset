s = str(input())
N = len(s)

max_won = N // 2
Top_won = 0
for i in range(N):
  if s[i] == "p":
    Top_won += 1
    
print(max_won - Top_won)