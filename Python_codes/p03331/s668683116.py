N = int(input())
temp_min = sum(map(int, str(1))) + sum(map(int, str(N - 1)))
for A in range (2, N):
    x = sum(map(int, str(A))) + sum(map(int, str(N - A)))
    if x < temp_min:
        temp_min = x
print(temp_min)