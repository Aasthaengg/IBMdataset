N = int(input())
K = int(input())
x = input().split()

sum = 0
for i in range(0,len(x)):
    if abs(K-int(x[i]))<int(x[i]):
        sum += abs(K-int(x[i]))*2
    else:
        sum += int(x[i])*2

print(sum)