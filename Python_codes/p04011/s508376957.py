x = [int(input()) for i in range(4)]
print(min(x[0], x[1])*x[2]+max(0, (x[0]-x[1]))*x[3])