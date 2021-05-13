N = int(input())
A, B = map(int, input().split())
Ps = list(map(int, input().split()))
n1 = 0
n2 = 0
n3 = 0
for P in Ps:
  if P <= A:
    n1 += 1
  if A+1 <= P <= B:
    n2 += 1
  if P >= B+1:
    n3 += 1
r = min(n1, n2, n3)
print(r)
