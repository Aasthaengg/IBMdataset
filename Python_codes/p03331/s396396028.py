N = int(input())
my_array = []
for A in range (1, N):
    my_array.append(sum(map(int, str(A))) + sum(map(int, str(N - A))))
print(min(my_array))