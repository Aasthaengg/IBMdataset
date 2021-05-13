N = int(input())
strX = input()

#10進数に変換
decX = int(strX,2)

#1の数をカウント
pop_c = strX.count('1')

# X % popcount+1
f_p = decX % (pop_c + 1)

# X % popcount-1(0になる時は0)
if pop_c == 1:
  f_m = 0
else:
  f_m = decX % (pop_c - 1)

for i in range(0,N):
  if strX[i] == '0':
    pop_a = (f_p + pow(2,(N-1-i),(pop_c + 1))) % (pop_c + 1) 
    Ans = 1
    
  elif pop_c == 1:
    pop_a = 0
    Ans = 0
    
  else:
    pop_a = f_m - (pow(2,(N-1-i),(pop_c - 1)))
    if pop_a < 0:
      pop_a = pop_a + pop_c - 1
    Ans = 1
  
  while pop_a > 0:
    wkpop = bin(pop_a).count('1')
    pop_a = pop_a % wkpop
    Ans += 1
  
  print(Ans)