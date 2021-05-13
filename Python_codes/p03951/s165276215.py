N = int(input())
A = input()
B = input()

for i in range(N):
  if A[i:] == B[0:N-i]:
    print(N+i)
    exit(0)
    
print(N*2)
