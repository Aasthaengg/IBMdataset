n,a,b = map(int,input().split())

def find_of_digits(num):
    sum = 0
    while num>0:
        sum += num % 10
        num //= 10

    return sum

total = 0
for i in range(1,n+1):
    s = find_of_digits(i)
    if s >= a and s <= b:
        total += i

print(total)