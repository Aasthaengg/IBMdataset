N = int(input())
s = list(input())
t = list(input())
c = 0
for i in range(1,N+1):
  if s[-i:] == t[:i]:
    if c <= i:
      c = i
print(2*N-c)