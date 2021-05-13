S=input()
T=input()

N=len(S)
F=False
for _ in range(N):
    S=S[-1]+S[:-1]
    F|=(S==T)

if F:
    print("Yes")
else:
    print("No")
