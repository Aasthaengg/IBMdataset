x, a, b = [int(i) for i in input().split()]
print("AB"[abs(x - a) > abs(x - b)])