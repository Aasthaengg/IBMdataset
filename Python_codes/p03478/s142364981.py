def FindSumOfDigits(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10       
    return s

inp = list(map(int,input().split()))
N = inp[0]
A = inp[1]
B = inp[2]
l=list()

sd = 0
for i in range(N+1):
    x = FindSumOfDigits(i)
    if A <= x <= B:
        sd = sd + i
    
print(sd)