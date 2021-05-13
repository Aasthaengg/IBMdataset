
N = int(input())

S = input()

strLen = len(S)

if strLen <= N :
    print(S)
else :
    result = S[0 : N]
    result += "..."
    print(result)