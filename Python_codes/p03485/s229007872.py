a,b=[int(i) for i in input().split()]
mean_ab=(a+b)/2
if (a+b)%2==0:
    print(int(mean_ab))
else:
    print(int(mean_ab)+1)