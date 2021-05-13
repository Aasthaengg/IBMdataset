k= int(input())
l = [i+(k//50) for i in range(51)]
del l[50-k%50]
print(50)
print(*l)