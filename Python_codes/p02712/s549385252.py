n = int(input())
FizzBuzz = []
for i in range(1,n+1):
    if not (i % 3 == 0) | (i % 5 == 0):
        FizzBuzz.append(i)
print(sum(FizzBuzz))