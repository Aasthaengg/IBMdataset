N, X, T = map(int, input().split()) 

time = 0
count = 1
while(1):
    sum = X* count
    if sum >= N:
        time = count*T
        break
    count += 1

print(time)