a,op,b = input().split()
d = {'+': 1, '-': -1}
print(int(a) + d[op] * int(b))