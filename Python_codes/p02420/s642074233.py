while True:
    S=[str(x) for x in input()]
    if S==["-"]:
        break
    else:
        l=len(S)
        m=int(input())
        for i in range(m):
            h=input()
            S=S[int(h):int(l+1)]+S[0:int(h)]
        print("".join(S))