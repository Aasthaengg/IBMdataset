#3問目
KT = input().split()
K,T = int(KT[0]), int(KT[1])
A = input().split()
intA = [int(s) for s in A]
saidai_i = 0
saidai = 0
withoutSaidaiSum = 0
for i in range(len(intA)):
    if(saidai < intA[i]):
        saidai = intA[i]
        saidai_i = i
for i in range(len(intA)):
    if(i != saidai_i):
        withoutSaidaiSum += intA[i]
print(max(0, saidai-withoutSaidaiSum-1))