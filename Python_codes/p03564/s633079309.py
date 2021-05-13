N_kai = int(input())
K = int(input())

current = 1

for i in range(N_kai):
    can_1 = current + K
    can_2 = current * 2
    
    current = min(can_1, can_2)

print(current)