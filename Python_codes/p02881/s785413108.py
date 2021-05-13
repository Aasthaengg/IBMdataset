import math
n = int(input())
mn = n+1
for num in range(1,int(math.sqrt(n)+1)) :
    if n%num == 0 :
        num2 = n // num
        mn = min(num+num2,mn)
print(mn-2)
