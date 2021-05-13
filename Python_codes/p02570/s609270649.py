x = input().split(' ')
x = list(map(int,x))
print("Yes") if (x[0]/x[1])<= x[2] else print("No")