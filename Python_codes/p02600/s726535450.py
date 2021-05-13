x = int(input())
l = [0,1800,1600,1400,1200,1000,800,600,400]
for i in range(1,9):
    if x >= l[i]:
        print(i)
        break