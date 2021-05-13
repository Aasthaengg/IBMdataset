
N = int(input())
s = 0
for i in range(1, N + 1):
    if i % 15 == 0:
        s = s # print("FizzBuzz")
    elif i % 3 == 0:
        s = s # print("Fizz")
    elif i % 5 == 0:
        s = s # print("Buzz")
    else:
        # print(i)
        s = s+i
print(s)
