A, B, C = map(int, input().split())
def diff(x,n, m):
  if x%2 == 0:
    return 0
  if x%2 == 1:
    return m*n
print(min([diff(A,B,C), diff(B,C,A), diff(C,A,B)]))