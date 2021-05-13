
N=int(input())
S=input()
T=input()
L=min(len(S), len(T))

count=0
for i in range(N):
    if S[-(i+1):]==T[:(i+1)]:
        count=(i+1)

print(len(S)+len(T)-count)