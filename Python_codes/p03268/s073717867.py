N,K = map(int,input().split())
Mod = [0 for i in range(K)]
for a in range(1,N+1):
    Mod[a%K] += 1
if K%2 == 1:
    Answer = Mod[0]**3
else:
    Answer = Mod[K//2]**3 + Mod[0]**3
print(Answer)