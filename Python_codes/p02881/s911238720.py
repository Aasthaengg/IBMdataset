n=int(input())

result = 10**12
for i in range(1,int(n**0.5)+1):
  if n % i == 0:
    result = min(result, i + n//i)

print(int(result-2))

