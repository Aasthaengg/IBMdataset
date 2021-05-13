N = int(input())
K = int(input())
x = list(map(int, input().split()))

all_length = 0
for pos in x:
    length = min(pos, K - pos)
    all_length += 2 * length
print(all_length)