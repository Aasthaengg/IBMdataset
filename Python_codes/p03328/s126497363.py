a, b = [int(num) for num in input().split()]
dif = b - a
hw = (dif-1)*dif/2
sol = hw - a
print(int(sol))