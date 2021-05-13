S = input()
K = int(input())
N = len(S)
#最初の1回
ans = 0
prev = S[0]
endchange = False
for i in range(1,N):
    if S[i] == prev:
        ans += 1
        prev = 0
        if i == N:
            endchange = True
    else:
        prev = S[i]

if all([s == S[0] for s in S]):
    print((N*K)//2)

elif K==1 or S[0] != S[-1]:
    print(ans * K)
else:
    front = 1
    while 1:
        if S[front] == S[0]:
            front += 1
        else:break
    back = -1
    while 1:
        if S[back] == S[0]:
            back -= 1
        else:break
    back = -1-back
    print(ans*K + ((front+back)//2 - front//2 - back//2) * (K-1))
