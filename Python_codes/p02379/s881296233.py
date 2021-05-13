x = list(map(float, input().split(' ')))
ans = pow((pow(x[0]-x[2], 2) + pow(x[1]-x[3], 2)), 0.5)
print("{0:.8f}".format(ans))
