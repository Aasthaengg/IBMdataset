x=[int(i) for i in input().split(" ")]
y="Yes" if x[0]**3==x[0]*x[1]*x[2] else "No"
print(y)