result = []

while True:
    first_input = int(input())
    if first_input == 0:
        break

    result.append(sum(list(map(int, str(first_input)))))

print(*result, sep='\n')

