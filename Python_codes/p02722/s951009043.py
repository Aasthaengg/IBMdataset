def Divisor(n):
    res = []
    for i in range(1, int(n**0.5)+1):
      if n % i != 0: continue
      res.append(i)
      if i*i != n: res.append(n//i)
    return res

n = int(input())

#K is a divisor of N
ans = 0
for x in Divisor(n):
    if x == 1: continue
    tmp = n
    while (tmp % x == 0):
        tmp /= x
    tmp %= x    
    if tmp == 1: 
      ans += 1
      
#K is not a divisor of N (except 1)
ans += len(Divisor(n-1))-1
print(ans)