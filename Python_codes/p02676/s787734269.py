
def ac_168b(K: int, S: str) -> str:
    if len(S) <= K:
        return S
    else:
        return S[0:K] + "..."

K = int(input())
S = input()
print(ac_168b(K, S))
