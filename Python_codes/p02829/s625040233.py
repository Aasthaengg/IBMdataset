A = int(input())
B = int(input())

l = [A, B]
for i in range(1, 4, 1):
  if i not in l:
    print(i)
    break