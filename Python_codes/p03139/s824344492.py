N, A, B = map(int,input().split())

if N > A+B:
  mini = 0
else:
  mini = A+B-N

print(str(min(A, B)) + " " + str(mini))