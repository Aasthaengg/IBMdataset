N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

C = 999
for i in H:
  tmp = T - 0.006 * i
  a = abs(tmp - A)
  if a < C:
    C = a
    x = int(H.index(i))+1
print(x)