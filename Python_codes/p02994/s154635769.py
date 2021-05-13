N,L = map(int,input().split())
min = 10**4
sum = 0
for i in range(N) :
    t = i+L
    sum += t
    if abs(t) < abs(min) :
        min  = t


print(sum - min)
