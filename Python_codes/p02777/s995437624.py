color=input().split()
number = list(map(int, input().split()))
c = input()
for i in range(2):
  if c == color[i]: number[i] -= 1
number = list(map(str, number))
print(' '.join(number))