while True:
    S = input()
    if S == "-":break
    m = int(input())
    sum = 0
    for i in range(m):sum+=int(input())
    if sum%len(S)==0:print(S)
    else:
        print(S[sum%len(S):]+S[:sum%len(S)])
