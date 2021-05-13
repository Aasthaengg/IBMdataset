n = int(input())
L= list(map(int,input().split()))
p = "Yes"
a = L[0]
for i in range(n-1):
  if L[i+1]+1 < a:
    p = "No"
  if a < L[i+1]:
    a = L[i+1]
print(p)