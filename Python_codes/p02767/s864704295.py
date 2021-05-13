n = int(input())
x = list(map(int, input().split()))
sum_energy_list = []

for p in range(1, 100):
    sum_energy = 0
    for i in range(len(x)):
        sum_energy += (x[i] - p) ** 2
    sum_energy_list.append(sum_energy)

answer = min(sum_energy_list)

print(answer)
