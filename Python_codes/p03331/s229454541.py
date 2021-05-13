N = int(input())

total = []
for i in range(1, N):
    x = sum(list(map(int, str(i)))) + sum(list(map(int, str(N - i))))
    total.append(x)

print(min(total))