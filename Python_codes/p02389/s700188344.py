num = input().split()
num_int = list(map(int, num))
menseki = num_int[0] * num_int[1]
nagasa = 2 * (num_int[0] + num_int[1])
print(menseki, nagasa)