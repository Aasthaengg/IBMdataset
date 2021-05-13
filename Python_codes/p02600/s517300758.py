def ranking(x):
    if(x>=400):
        if(x<600):
            return 8
        elif(x<800):
            return 7
        elif (x < 1000):
            return 6
        elif (x < 1200):
            return 5
        elif (x < 1400):
            return 4
        elif (x < 1600):
            return 3
        elif (x < 1800):
            return 2
        elif (x < 2000):
            return 1
x=int(input())
print(ranking(x))