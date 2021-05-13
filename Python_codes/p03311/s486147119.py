n = int(input())
A = list(map(int,input().split()))
A = [j-i-1 for i,j in enumerate(A)]
top = max(A)
bottom = min(A)
def sad(b):
  ret=0
  for i in A:
    ret += abs(i-b)
  return ret
while top - bottom > 2:
  mid1 = (top + bottom*2)//3
  mid2 = (top*2 + bottom)//3
  if sad(mid1) < sad(mid2):
    top = mid2
  else:
    bottom = mid1
print(min(sad(bottom), sad((bottom+top)//2), sad(top)))
