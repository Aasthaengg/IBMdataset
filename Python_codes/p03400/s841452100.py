N = int(input())
D,X = map(int,input().split())
A = [int(input()) for i in range(N)]
sum = N

for i in A:
    day = i
    d = 1
    while day <= D:
        day = d*i+1
        d += 1
        if day <= D:
            sum += 1
        else:
            break

sum += X
print(sum)