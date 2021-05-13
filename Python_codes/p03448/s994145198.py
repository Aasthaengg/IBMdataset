a = int(input())
b = int(input())
c = int(input())
x = int(input())

answer = 0
for coin1 in range(a+1):
    for coin2 in range(b+1):
        for coin3 in range(c+1):
            if x == 500 * coin1 + 100 * coin2 + 50 * coin3:
                answer += 1

print(answer)