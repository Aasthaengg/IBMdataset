n,k = map(int,input().split())
s = input()
taboo = '1' * k
for i in range(n-k+1):
  if s[i:i+k] == taboo:
    print(-1)
    break
else:
  s = s[::-1]
  #print(s)
  ans = []
  now = 0
  while True:
    for i in range(k):
      if now + k - i <= n:
        if s[now+k-i] == '0':
          now += k-i
          ans.append(k-i)
          #print(ans)
          break
    if now == n:
      ans.reverse()
      print(' '.join(list(map(str,ans))))
      break