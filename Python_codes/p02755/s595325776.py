A, B = map(int, input().split())
target = -1
for i in range(1300):
  if int(i*0.08) == A and int(i*0.1) == B:
    target = i
    break
print(target)
