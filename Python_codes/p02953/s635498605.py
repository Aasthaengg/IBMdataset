N = int(input())
H = list(map(int, input().split()))

ans = 'Yes'
for i in range(1, N):
  if H[N-i-1]-1 == H[N-i]:
    H[N-i-1] -= 1
  elif H[N-i-1]-1 > H[N-i]:
    ans = 'No'
    break
    
print(ans)