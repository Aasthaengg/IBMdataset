S=str(input())

numbs=len(S)
nin=10**3
for i in range(numbs-2):
    nin=min(nin,abs(753-int(S[i:i+3])))
print(nin)
