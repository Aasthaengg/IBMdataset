N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [0]*N
count = 0

def a_x_b(ab):
  a, b = ab
  return a*b

for n in range(N):
  A[n] = list(map(int, input().split()))
  AB = [(A[n][i], B[i]) for i in range(M)]
  if sum(list(map(a_x_b, AB)))+C > 0:
    count += 1
  else:
    continue
    
print(count)