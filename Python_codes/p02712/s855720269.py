n = int(input())
s = 0

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    else:
        s += i
    #print(i)

print(s)