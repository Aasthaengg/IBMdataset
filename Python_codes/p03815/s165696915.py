X = int(input())
Count = 2*(X//11)
RestX = X-11*(X//11)
print(Count+[0,1,2][(RestX>=1)+(RestX>=7)])