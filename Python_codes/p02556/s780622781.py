N = int(input())
z = [0] * N
w = [0] * N
for i in range(N):
  x, y = map(int, input().split())
  z[i] = x + y
  w[i] = x - y
  
z = sorted(z)
w = sorted(w)
#print(z)
#print(w)
ans = max(abs(z[-1] - z[0]), abs(w[-1] - w[0]))
print(ans)