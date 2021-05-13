N = int(input())
s = input()
t = input()

if t in s:
  print(N)
  quit()

for i in range(1, N+1):
  if t in (s + t[-i:]):
    print(N+i)
    quit()