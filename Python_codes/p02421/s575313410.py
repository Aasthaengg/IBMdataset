n = int(input())
t_point = 0
h_point = 0
for i in range(n):
    card = input().split()
    taro = card[0]
    card.sort()
    card.reverse()
    if card[0] == card[1]:
        t_point += 1
        h_point += 1
    elif card[0] == taro:
        t_point += 3
    else:
        h_point += 3

print(t_point,h_point)