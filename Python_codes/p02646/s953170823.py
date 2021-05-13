A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

speed = V - W
length = abs(B - A)

if length <= T * speed:
  print('YES')
else:
  print("NO")
