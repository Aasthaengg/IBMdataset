# 横か縦か。各時点でn-2 or n-1C2
# str1だけ見ればよい

N = int(input())
txt = input()

pattern = []
j = 0

while j < N:
  if j == N-1 or txt[j] != txt[j+1]:
    pattern.append(1)
    j += 1
  else:
    pattern.append(2)
    j += 2


    
MOD = 10**9 + 7

ans = 3 if pattern[0] == 1 else 6
for j in range(1,len(pattern)):
  a,b = pattern[j-1:j+1]
  if (a,b) == (1,1):
    ans *= 2
  elif (a,b) == (1,2):
    ans *= 2
  elif (a,b) == (2,1):
    ans *= 1
  else:
    ans *= 3
  ans %= MOD

print(ans)
