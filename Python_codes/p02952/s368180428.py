n = input()
size = len(n)
n = int(n)
i = 1
ans = 0
while 2*i-1 < size:
  ans = ans + 9*(10**(2*i-2))
  i = i+1
if size%2==1:
  ans = ans + (n-10**(size-1)) + 1
  
print(ans)