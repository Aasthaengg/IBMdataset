K = int(input())
A, B = map(int, input().split())

check = False
for i in range(A, B+1):
  if i % K == 0:
    check = True
    
print("OK" if check else "NG")