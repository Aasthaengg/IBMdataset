N = int(input())
ans = ''

for i in range(1, 100):
  if N <= 26**i:
    N = N - 1
    for j in range(i):
      ans += chr(ord('a')+ N % 26)
      N = N // 26
    break
  else:
    N = N - 26**i
    
print(ans[::-1])
