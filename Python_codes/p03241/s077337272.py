import math
N,M = map(int, input().split())
#約数列挙
flag = True
yakusuu = []
for i in range(1, math.floor(math.sqrt(M))+1):
    if(M % i == 0):
        yakusuu.append(i)
        yakusuu.append(int(M / i))
yakusuu.sort()
yakusuu.reverse()
for i in yakusuu:
    if M / i >= N and flag == True:
        print(i)
        flag = False