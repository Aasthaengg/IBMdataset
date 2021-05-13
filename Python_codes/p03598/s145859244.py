N = int(input())
K = int(input())
X= [int(i) for i in input().split()]
Sum = 0
for x in X:
    if x < abs(x-K):
        Sum += 2*x
    else:
        Sum += abs(x-K)*2
print(Sum)