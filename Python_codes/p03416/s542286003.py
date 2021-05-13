A, B = map(int, input().split())

sum = 0

for n in range(A, B+1):
    rev = 0
    m = n
    while n != 0:
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    if(m == rev):
        sum += 1
print(sum)

