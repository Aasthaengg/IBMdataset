x=int(input())
y=100
for i in range(3760):
    y=101*y//100
    if y>=x:
        print(i+1)
        exit()