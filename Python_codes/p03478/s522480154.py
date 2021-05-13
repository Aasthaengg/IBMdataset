N,A,B=input().split()
N=int(N)
A=int(A)
B=int(B)

def findSumOfDigits(n):
    k = 0
    sum = 0
    while n>0:
        k = n%10
        n = n//10
        sum = sum + k
    return sum

sum=0
for i in range(N+1):
    tmp = findSumOfDigits(i)
    if A<=tmp:
        if tmp<=B:
            sum = sum + i
print(sum)
