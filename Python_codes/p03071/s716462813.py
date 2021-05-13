x = list(map(int, input().split()))
if x[0] == x[1]:
    print(x[0]+x[1])
elif x[0] > x[1]:
    print(x[0]+(x[0]-1))
elif x[0] < x[1]:
    print(x[1]+(x[1]-1))
