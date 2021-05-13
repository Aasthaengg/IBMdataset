from collections import Counter
N = int(input())
A = list(map(int, input().split()))


def xor_circle(N, A):
    if sum(A) == 0:
        return "Yes"
    if N % 3 != 0:
        return "No"

    B = Counter(A)
    if len(B) == 3:
        a, b, c = B.keys()
        Na, Nb, Nc = B.values()
        if a ^ b ^ c == 0 and Na == Nb == Nc:
            return "Yes"
        else:
            return "No"
    elif len(B) == 2:
        a, b = B.keys()
        Na, Nb = B.values()
        if a == 0 and 2*Na == Nb:
            return "Yes"
        elif b == 0 and Na == 2*Nb:
            return "Yes"
        else:
            return "No"
    else:
        return "No"


ans = xor_circle(N, A)
print(ans)
