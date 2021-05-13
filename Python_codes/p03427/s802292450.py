N = str(input())
l = len(N)
if N[1:] == '9'*(l-1):
  ans = int(N[0]) + 9*(l-1)
else:
  ans = int(N[0])-1 + 9*(l-1)
print(ans)