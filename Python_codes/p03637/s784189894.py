N = int(input())
A = [int(x) for x in input().split()]
n1 = 0
n2 = 0
n4 = 0

for a in A:
  if a&1:
    n1 += 1
  elif a%4==0:
    n4 += 1
  else:
    n2 += 1

 
bl = True
# n1 <= n4なら、141414と並べてあとは適当
if n1 > n4:
  #1414...141のときだけ
  if not(n1 == n4 + 1 and n2 == 0):
    bl = False

answer = 'Yes' if bl else 'No'
print(answer)
