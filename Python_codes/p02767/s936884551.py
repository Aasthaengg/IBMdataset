N = int(input())
pd = [0]*100
*X, = map(int,(input().split()))
for i in range(100):
    x_sum = 0
    for j in X:    
        y = (j-i)**2
        x_sum += y
    pd[i-1] = x_sum
print(min(pd))