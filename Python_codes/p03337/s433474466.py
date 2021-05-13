x = list(map(int,input().split()))

print(str(max(int(x[0])+int(x[1]),int(x[0])*int(x[1]),int(x[0])-int(x[1]))))