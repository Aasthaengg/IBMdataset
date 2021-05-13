S = input()
ans = len(S) * (len(S)-1) // 2 + 1

for ch in 'abcdefghijklmnopqrstuvwxyz':
  n = S.count(ch)
  if n>0:
    #print(ch,n)
    ans -= n * (n-1) // 2
    
print(ans)