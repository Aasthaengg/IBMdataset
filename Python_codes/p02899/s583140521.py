N = int(input())
A = [int(i) for i in input().split()]
A_tupple = [(idx+1, value) for idx, value in enumerate(A)]
A_tupple.sort(key=lambda x:x[1])
for a in A_tupple:
  print(a[0], end=" ")
