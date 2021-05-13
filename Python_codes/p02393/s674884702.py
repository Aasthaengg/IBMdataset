x = raw_input().split()
for i in range(2):
    if float(x[i]) > float(x[i+1]):
        x[i],x[i+1]=x[i+1], x[i]
    if float(x[0]) > float(x[1]):
        x[0],x[1]=x[1], x[0]
print " ".join(x)