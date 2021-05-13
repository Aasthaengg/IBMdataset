N = int(input())
x= [""]*(N+1)
u= [""]*(N+1)

for i in range(N):
  x[i],u[i] = input().split()

sum = 0
for i in range(N):
  sum += float(x[i]) if u[i] == "JPY" else float(x[i])*380000.0

  
print(sum)