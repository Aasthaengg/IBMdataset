N = int(input())
count = 0
for i in range(1, N):
    if i != N - i and i < N/2:
        count = count + 1
print(count)