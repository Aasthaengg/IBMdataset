
X,Y=open(0).read().split()

X=int(X)

Y=int(Y)


for i in range(110000):
    if (2**i) >= 1000000000000000000:
        #print(i)
        break



list1=[2**i*X for i in range(61) if 2**i*X <= Y]

print(len(list1))
