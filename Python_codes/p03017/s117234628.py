N,A,B,C,D = map(int,input().split())
S = input()
S = S[A-1:]
B -= A
C -= A
D -= A
A = 0

kabe = S.find("##")
if kabe != -1:
    if kabe < C or kabe < D:
        print('No')
        exit()
if C < D:
    print('Yes')
else:
    A = S[:B].rfind(".")
    S = S[A:]
    B -= A
    C -= A
    D -= A
    A = 0
    irekae = S.find("...")
    if irekae == -1:
        print('No')
        exit()
    if irekae + 2 <= C and irekae < D:
        print('Yes')
    else:
        print('No')
