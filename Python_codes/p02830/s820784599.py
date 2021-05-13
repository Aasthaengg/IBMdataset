N = int(input())
S,T = input().split()

for i in range(N):
    print(S[i:i+1]+T[i:i+1],end="")