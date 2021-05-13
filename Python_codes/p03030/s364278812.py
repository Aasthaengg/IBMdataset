for x in [j[0] for j in sorted([[i+1,*input().split()] for i in range(int(input()))],key=lambda x: (x[1], -int(x[2])))]:
     print(x)