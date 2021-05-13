ABC = [int(input()) for _ in range(3)]
X = int(input())

A,B,C = ABC[0],ABC[1],ABC[2]

ans = 0
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      if i * 500 + j * 100 + k * 50 == X:
        ans += 1
        
print(ans)
        
