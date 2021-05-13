n = int(input())
ai = [int(x) for x in input().split()]

ai.sort()

temp = [abs(x) for x in ai[1:-1]]

o1 = -ai[0] + sum(temp) + ai[-1]

print(o1)

temp1 = ai.pop(-1)
num_p = sum(x >= 0 for x in ai)
if num_p == len(ai):
  num_p -= 1
for i in range(num_p):
  temp2 = ai.pop(-1)
  print(ai[0], temp2)
  ai[0] -= temp2

for i in range(len(ai)):
  temp2 = ai.pop(0)
  print(temp1, temp2)
  temp1 -= temp2
 
