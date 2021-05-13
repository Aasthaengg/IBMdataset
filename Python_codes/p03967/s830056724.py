s = list(input())
N = len(s)

#(方針)パーが使えるようになった瞬間パー使用 → gpgpgpgp...
win = 0
lose = 0
for i in range(N):
  if(i%2 == 0): #奇数回目 g
    my_hand = 'g'
    if(my_hand != s[i]): lose += 1 #負け
  else: #偶数回目 p
    my_hand = 'p'
    if(my_hand != s[i]): win += 1 #負け
  
ans = win-lose
print(ans)