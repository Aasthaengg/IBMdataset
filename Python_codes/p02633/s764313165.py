X = int(input())
n = 2
k = 0

k = 360//X
while(360*(n-1) % X != 0):
    k = (360*n)//X
    n += 1

print(k)