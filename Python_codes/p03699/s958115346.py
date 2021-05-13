N = int(input())
S = []
for i in range(N):
    S.append(int(input()))
nb10 = ([s for s in S if s%10 != 0])
b10  = ([s for s in S if s%10 == 0])
    
if sum(S)%10!=0:
    print(sum(S))
elif sum(S) ==sum(b10):
    print(0)
else:

    print(sum(S)-sorted(nb10)[0])