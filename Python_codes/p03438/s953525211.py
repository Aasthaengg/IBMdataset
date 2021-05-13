N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

#print(A)
#print(B)

x=y=0
for i in range(len(A)):
  a, b = A[i], B[i]

  if a<b: x+=(b-a)//2*2
  if a>b: y+=a-b

ans="Yes" if x >= y*2 else "No"
print(ans)