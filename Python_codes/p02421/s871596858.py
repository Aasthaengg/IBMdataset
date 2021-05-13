t_point, h_point = 0, 0

n = int(input())
for i in range(n):
    t_card, h_card = input().split()
    if t_card == h_card:
        t_point += 1
        h_point += 1
    elif t_card > h_card:
        t_point += 3
    else:
        h_point += 3
print(t_point, h_point)