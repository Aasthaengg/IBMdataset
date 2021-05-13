S = list(input())
# i = 2
while S != []:
    S.pop()
    S.pop()
    l = len(S)
    half = int(l / 2)
    # print(S)
    # print(S[0:half])
    # print(S[half:])
    if S[0:half] == S[half:]:
        print(l)
        exit()