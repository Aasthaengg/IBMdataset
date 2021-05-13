N, M, C = list(map(lambda x: int(x), input().split(" ")))
B = list(map(lambda b: int(b), input().split(" ")))
cnt = 0
for i in range(N):
  A = list(map(lambda a: int(a), input().split(" ")))
  if sum([a * b for (a, b) in zip(A, B)]) + C > 0:
    cnt += 1
    
print(cnt)