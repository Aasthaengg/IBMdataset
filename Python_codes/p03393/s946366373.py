S = str(input())
l = [chr(i) for i in range(97,97+26)]

flag = True
for s in l:
  if s not in S:
    ans = S + s
    flag = False
    break
    
if flag:
  if S == 'zyxwvutsrqponmlkjihgfedcba':
    ans = -1
  else:
    while flag:
      num = ord(S[-1])
      S = S[:-1]
      for n in range(num+1, 123):
        if chr(n) not in S:
          ans = S + chr(n)
          flag = False
          break
    
print(ans)