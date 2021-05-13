check=[99, 111, 222, 333, 444, 555, 666, 777, 888, 999]

n=int(input())

if n in check:
    print(n)
else:
    for i in range(20):
        if check[i]<n<check[i+1]:
            print(check[i+1])
            exit()