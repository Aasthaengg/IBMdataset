import sys
input = sys.stdin.readline

S = list(input().rstrip('\n'))
# print(S[2:-1])
if S[0] == 'A' and S[2:-1].count('C') == 1:
    S.remove('A')
    S.remove('C')
    S = ''.join(S)
    # print(S)
    if S.islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")
