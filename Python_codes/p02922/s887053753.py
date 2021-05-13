A, B = map(int, input().split())
N = 1
i = 0
while N < B:
  N += A-1
  i += 1  
print(i)
