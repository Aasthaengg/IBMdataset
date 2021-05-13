N = int(input())
S = input()

T = S[:int(len(S)/2)]

S_alt = T + T

if S == S_alt:
    print("Yes")
else:
    print("No")