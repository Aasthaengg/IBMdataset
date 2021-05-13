# ABC149 C - Next Prime

x = int(input())
for i in range(x,10**5+4):
    if all(i%j!=0 for j in range(2,x)):
        print(i)
        break