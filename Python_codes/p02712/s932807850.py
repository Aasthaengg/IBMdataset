N = int(input())
l = []
n = 0
for i in range(1,N+1):
    if i%3==0 and i%5==0:
        l.append('FizzBuzz')
    else:
        if i%3==0:
            l.append('Fizz')
        elif i%5==0:
            l.append('Buzz')
        else:
            l.append(i)
            n += i
print(n)