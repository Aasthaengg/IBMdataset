N = int(input())
S = input()
T = input()

if S==T:
    print(N)
    exit()
for i in range(N):
    if S[i:] == T[:-i]:
        print(N+i)
        exit()
print(N+N)