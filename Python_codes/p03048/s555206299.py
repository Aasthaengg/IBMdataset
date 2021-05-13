R,G,B,N = map(int, input().split())
ans = 0
for i in range(N//R+1):
  for j in range((N-i*R)//G+1):
    b = (N-R*i-G*j)/B
    if b%1 == 0 and b >= 0:
      ans += 1
print(ans)