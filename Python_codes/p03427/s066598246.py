N = input()
n = len(N)

if N[1:] == "9"*(n-1):
  ans = int(N[0])+9*(n-1)
else:
  ans = int(N[0])-1 + 9*(n-1)

print(ans)