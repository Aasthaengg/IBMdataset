#  ABC 088 B - Card Game for Two
N = int(input())
an = list(map(int, input().split()))

Alice = []
Bob = []
while len(an) > 0:
    Alice.append(max(an))
    del an[an.index(max(an))]
    if len(an) > 0:
        Bob.append(max(an))
        del an[an.index(max(an))]
    else:
        break

k = 0
j = 0
for i in range(len(Alice)):
    k += Alice[i]
for i in range(len(Bob)):
    j += Bob[i]

print(str(k-j))