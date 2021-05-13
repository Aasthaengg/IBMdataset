W,a,b = [int(i) for i in input().split()]

if a - W <= b and a + W >= b:
    print(0)
elif a - W > b:
    print(a - b - W)
elif a + W < b:
    print(b - a - W)
