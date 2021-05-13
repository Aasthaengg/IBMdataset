import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

key_1, key_4 = 0, 0
for value in a:
  if value%4 == 0:
    key_4 += 1
  elif value%2 == 1:
    key_1 += 1

if key_4+key_1 == n and key_1 <= key_4+1:
  print("Yes")
elif key_1 <= key_4:
  print("Yes")
else:
  print("No")