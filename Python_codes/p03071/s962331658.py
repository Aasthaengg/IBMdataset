x=[int(i) for i in input().split()]
x.append(x[0]-1)
x.append(x[1]-1)
x.sort()
print(sum(x[2:]))