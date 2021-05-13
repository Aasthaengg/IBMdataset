N = int(input())
S = input()

result = 0
for i in range(0, 1000):
    number = ''.join(['00', str(i)])[-3:]
    number_i = 0
    for s in S:
        if number[number_i] == s:
            number_i += 1
            if number_i == 3:
                result += 1
                break

print(result)
