N = int(input())
S = list(str(input()))

if N %2 == 1:
    print('No')
    exit()
for i in range(int(N//2)):
    if S[i] != S[N//2+i]:
        print('No')
        exit()
print('Yes')