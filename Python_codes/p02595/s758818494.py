import math

N,D =  map(int,input().split())

result_count = 0;

for i in range(N):
    X,Y = map(int,input().split())

    distance = math.sqrt((X**2) + (Y**2))

    if(distance <= D):
        result_count += 1

print(result_count)
