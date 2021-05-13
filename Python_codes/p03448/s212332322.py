in_a = input()
in_b = input()
in_c = input()
in_x = input()

A = int(in_a)
B = int(in_b)
C = int(in_c)
X = int(in_x)

count = 0
for i in range(A+1):
    for j in range(B+1):
        k = ( X - 500*i - 100*j ) / 50
        # print(f'k：{k}')
        if k < 0:
            break;
        elif k.is_integer() and k <= C:
            count +=1
            # print('clear', k, count)

print(count)