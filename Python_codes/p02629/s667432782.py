N = int(input())

number = N
answer = ''

while number >= 1:
    x = number % 26
    if x == 0:
        x = 26
        number -= 26

    answer = chr(96+x) + answer

    number //= 26

print(answer)