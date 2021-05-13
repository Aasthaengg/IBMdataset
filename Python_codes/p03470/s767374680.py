N = int(input())

X = [int(input()) for _ in range(N)]

size_dict = {}

for x in X:
    size_dict[x] = 1

ans = len(size_dict.keys())

print(ans)