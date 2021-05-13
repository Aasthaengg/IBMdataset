S, T = input().split()
a, b =map(int, input().split()) 
U = input()
if S == U:
  a -= 1
if T == U:
  b -= 1
print(a, b)