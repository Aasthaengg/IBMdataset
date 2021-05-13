A, B, K = map(int, input().split())

cnt = 0
while cnt < K:
  A = A // 2
  B = B + A
  cnt += 1
  #print(cnt,A,B)
  if cnt >= K:
    break
  
  B = B // 2
  A = A + B
  cnt += 1
  #print(cnt,A,B)
  
print(A,B)