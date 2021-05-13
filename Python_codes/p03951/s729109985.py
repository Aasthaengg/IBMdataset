N = int(input())
S = input()
T = input()
ans = S+T
for i in range(1,N+1):
    #print(S[-i:],T[:i])
    if S[-i:] == T[:i]:
        ans = S + T[i:]
print(len(ans))