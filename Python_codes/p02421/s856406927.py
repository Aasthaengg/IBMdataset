taro = 0
hanako = 0
n = int(input())
for _ in range(n):
    t_c, h_c = input().strip().split()
    if t_c < h_c:
        hanako += 3
    elif t_c == h_c:
        taro += 1
        hanako += 1
    else:
        taro += 3
print ('{} {}'.format(taro, hanako))
