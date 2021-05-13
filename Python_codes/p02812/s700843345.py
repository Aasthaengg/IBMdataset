N = int(input())
S = input()

# 任意のi(0≤i≤n-3)について、S[i]以下3文字が'ABC'であるかを確認すればよい
ans = 0
for i in range(N-2):
  if S[i:i+3] == 'ABC': ans += 1
    
print(ans)