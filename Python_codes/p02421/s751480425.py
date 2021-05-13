n = int(input())

T_s = 0
H_s = 0

for i in range(n):
    animals = input().split()
    T_a = animals[0]
    H_a = animals[1]
    if T_a < H_a:
        H_s += 3
    elif T_a > H_a:
        T_s += 3
    else:
        T_s += 1
        H_s += 1

print(T_s, H_s)