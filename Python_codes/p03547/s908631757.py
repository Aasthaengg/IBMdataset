S = list(map(str, input().split()))
if S[0] == S[1]:
    print("=")
    exit()
if S == sorted(S):
    print("<")
else:
    print(">")