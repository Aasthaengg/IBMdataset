import collections
N = int(input())
V = list(map(int,input().split()))
E = []
O = []
for i in range(N):
    if i % 2 == 0:
        O.append(V[i])
    else:
        E.append(V[i])
EC = collections.Counter(E).most_common()
OC = collections.Counter(O).most_common()
if len(EC) == 1 and len(OC) == 1:
    if EC[0][0] == OC[0][0]:
        print(N//2)
    else:
        print(0)
elif len(EC) == 1 and len(OC) != 1:
    if EC[0][0] == OC[0][0]:
        print(N-EC[0][1]-OC[1][1])
    else:
        print(N//2-OC[0][1])
elif len(EC) != 1 and len(OC) == 1:
    if EC[0][0] == OC[0][0]:
        print(N//2-EC[1][1])
    else:
        print(N//2-EC[0][1])
elif EC[0][0] == OC[0][0]:
    if EC[0][1]+OC[1][1] == EC[1][1]+OC[0][1]:
        print(N-EC[0][1]-OC[1][1])
    elif EC[0][1]+OC[1][1] > EC[1][1]+OC[0][1]:
        print(N-EC[0][1]-OC[1][1])
    else:
        print(N-EC[1][1]-OC[0][1])
else:
    print(N-EC[0][1]-OC[0][1])