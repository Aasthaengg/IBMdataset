while(True):
    S=input()
    if S=="-":
        break
    N=int(input())
    h=[int(input()) for i in range(N)]
    for i in range(N):
        S=S[h[i]:]+S[:h[i]]
    print(S)

