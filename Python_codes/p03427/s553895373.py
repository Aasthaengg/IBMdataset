N = [int(i) for i in input()]
a = sum(N)
b = 9 * (len(N) - 1) + N[0] - 1
print(max(a,b))