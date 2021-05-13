import numpy as np

n = int(input())
a = np.array(list(map(int,input().split())))

count = 0
while np.all(a%2==0):
    count+=1
    a=a/2
print(count)
