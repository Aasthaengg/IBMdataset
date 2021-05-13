A, B, N = map(int, input().split())
cnt = min(B-1, N)
result = int(A*cnt/B)-A*int(cnt/B)
  
print(result)