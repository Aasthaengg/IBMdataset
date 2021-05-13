str = input().split(" ")
S = str[0]
T = str[1]
num = input().split(" ")
NS = int(num[0])
NT = int(num[1])
U = input()

if S == U:
  print(NS - 1, end=" ")
  print(NT)
else:
  print(NS, end=" ")
  print(NT - 1)