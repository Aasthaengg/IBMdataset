r, D, x2000 = map(int,input().split())

lst = [x2000]

x = 0
for i in range(10):
    x = r*lst[i] - D
    lst.append(x)
    print(x)
