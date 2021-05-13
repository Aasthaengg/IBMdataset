S = input()
w = int(input())
ans = ''
now = 0
while now <= len(S)-1:
  ans += S[now]
  now += w
  
print(ans)