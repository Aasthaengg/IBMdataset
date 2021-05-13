def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)                
                
    divisors.sort()
    return divisors

n = int(input())
num = 0

num += len(make_divisors(n-1))-1

k = make_divisors(n)
k.pop(0)

for item in k:
  tn = n
  while tn % item == 0:
      tn /= item
    
  if tn % item == 1:
    num += 1

print(num)
