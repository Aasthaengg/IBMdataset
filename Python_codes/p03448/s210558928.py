import sys
input = sys.stdin.readline

coin_count = [int(input()) for _ in range(3)]
X = int(input())

result = 0
for i in range(min(X//500, coin_count[0]) + 1):
    for j in range(min((X - 500*i)//100, coin_count[1]) + 1):
        if 500 * i + 100 * j + 50 * coin_count[2] >= X:
            result += 1
print(result)