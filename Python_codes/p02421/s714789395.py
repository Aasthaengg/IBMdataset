n = int(input())
T_point = H_point = 0
for _ in range(n):
    T_card,H_card = [x for x in input().split()]
    if T_card > H_card:
        T_point += 3
    elif T_card < H_card:
        H_point += 3
    else:
        T_point += 1
        H_point += 1
print(T_point,H_point)

