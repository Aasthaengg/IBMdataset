n,a,b = map(int,input().split(' '))

sum = 0
for i in range(n+1):
    digitSum = 0
    digitCheck = i
    while digitCheck>0:
        digitSum += digitCheck%10
        digitCheck = digitCheck//10
    if a <= digitSum <= b:
        sum +=i
    
    
print(sum)