from itertools import product
X, Y, Z, K = map(int, input().split())
AB = []
for ab in product(map(int, input().split()), map(int, input().split())):
    AB.append(ab[0] + ab[1])
AB.sort(reverse=True)
AB = AB[:min(K,X*Y)]
ABC = []
for abc in product(AB, map(int, input().split())):
    ABC.append(abc[0]+abc[1])
ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])
