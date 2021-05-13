N = int(input())
s = set()
dic = {}
memo = [0]*(N+1)
sm = {}
memo[0] = 1
P = 10**9 + 7
b = 0

for i in range(1,N+1):
  c = int(input())
  if c not in s:
    s.add(c)
    dic[c] = [i]
    memo[i] = memo[i-1]
  else:
    memo[i] = memo[i-1]
    if b != c:
      if len(dic[c]) == 1:
        sm[c] = memo[dic[c][0]-1]
      else:
        sm[c] += memo[dic[c][-1]-1]
      memo[i] += sm[c]
      memo[i] %= P
      dic[c].append(i)
  b = c
      
print(memo[N])