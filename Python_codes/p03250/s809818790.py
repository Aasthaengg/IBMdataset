n= [int(s) for s in input().split()]
n.sort()
max_value = n[2] * 10 + n[1] + n[0]

print(max_value)