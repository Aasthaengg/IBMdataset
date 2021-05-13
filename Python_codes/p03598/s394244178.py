N = int(input())
K = int(input())
X = [int(x) for x in input().split()]

distance = []
for x in X:
    if x < abs(K-x):
        distance.append(x)
    else:
        distance.append(abs(K-x))

print(2*sum(distance))