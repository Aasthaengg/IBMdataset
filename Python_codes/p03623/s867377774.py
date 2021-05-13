x,a,b = map(int, input().split())

dis_a = abs(x-a)
dis_b = abs(x-b)

if dis_a <= dis_b:
    print("A")
else:
    print("B")