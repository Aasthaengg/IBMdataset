X = int(input())
flag = False
for i in range(1, X+1):
    if 100*i <= X <= 105*i:
        flag = True
        break
print('1' if flag else '0')
