r, D, x_2000 = map(int,input().split())

tmp = x_2000
for i in range(1,11):
    tmp = r * tmp - D
    print(tmp)
