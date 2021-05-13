a,b,k = map(int, input().split())
for i in range (k):
  if a + i <= b-k:
    print(str(a+i))
for i in range (k):
  if a <= b+1-k+i: 
    print(str(b+1-k+i))