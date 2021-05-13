n = int(input())
a = list(map(int, input().split()))
a0 = [0]+a+[0]
suma = 0
for i in range(n+1):
  suma += abs(a0[i+1]-a0[i])

for i in range(1, n+1):
  if (a0[i]-a0[i-1])*(a0[i+1]-a0[i]) >= 0:
    print(suma)
  else:
    print(suma-abs(a0[i]-a0[i-1])-abs(a0[i+1]-a0[i])+abs(a0[i+1]-a0[i-1]))