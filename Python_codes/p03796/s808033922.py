n = int(input())
answer = 1
for index in range(1, n+1):
    answer = (answer * index) % (10 ** 9 + 7)

print(answer)