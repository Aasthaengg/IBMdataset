N = int(input())
x = [0] * (N+1)
y = [0] * (N+1)
t = [0] * (N+1)
for i in range(N):
    a,b,c = map(int, input().split())
    t[i+1] = a
    x[i+1] = b
    y[i+1] = c

a = 'Yes'
for i in range(N):
    if t[i+1] - t[i] < abs(x[i+1]-x[i]) + abs(y[i+1] - y[i]):
      a = 'No'
      break
    if (t[i+1] - t[i]) % 2 != (abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])) % 2:
      a = 'No'
      break
print(a)