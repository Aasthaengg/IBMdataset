N = int(input())
A = list(map(int, (input() for i in range(N))))
B = sorted(A, reverse=True)
a = B[0]
a1 = B[1]


for x in A:  
  if x != a:
    print(a)
  else:
    print(a1)