N,A,B = map(int,input().split())
p = 0

def digitSum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


for i in range(1,N+1):
    if A <= digitSum(i) <= B:
        p+=i
        
print(p)

