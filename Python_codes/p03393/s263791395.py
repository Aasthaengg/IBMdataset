import sys
input = sys.stdin.readline

S = input()

alphabets = set(chr(ord('a')+x) for x in range(26))

def F(S,alphabets):
    if len(S) == 0:
        return -1
    T = F(S[1:],alphabets-set([S[0]]))
    if T == -1:
        larger = [x for x in alphabets if x > S[0]]
        if not larger:
            return -1
        return min(larger)
    return S[0] + T

answer = F(S,alphabets)
print(answer)
