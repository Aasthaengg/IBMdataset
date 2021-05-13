n, a, b = map(int, input().split()) 

result = 0

def check(n):
    sum = 0
    while n>0 :
        sum += n%10
        n//=10
    return sum

for i in range(n):
    x = check(i+1)
    if a <= x and x <= b:
        result += i+1

print(result)