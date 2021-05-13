n,k = map(int,input().split())

s=list(input())

memo = [0]

for i in range(1,n):
  if s[i] != s[i-1]:
    memo.append(i)

ans = 0

kyoukai_math = len(memo)

for i in range(kyoukai_math):
  if s[memo[i]] == '1':
    hasi = i+k*2+1
  else:
    hasi = i+k*2
    
  if hasi < kyoukai_math:
    ans = max(ans,memo[hasi]-memo[i])
  else:
    ans = max(ans,n-memo[i])
print(ans)