N = int(input())

a = [i for i in range(1,N + 1)]

ans = 0

for i in range(N):
  if a[i]%15 == 0:
    a[i] = "FizzBuzz"
  elif a[i]%3 == 0:
    a[i] = "Fizz"
  elif a[i]%5 == 0:
    a[i] = "Buzz"
    
for i in a:
  if type(i) == int:
    ans += i
    
print(ans)