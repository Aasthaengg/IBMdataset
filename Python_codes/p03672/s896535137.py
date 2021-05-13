S = input()

def solve(S):
    for i in range(len(S)):
        S = S[:-1]
        if len(S) % 2 == 1:
            continue
        half = len(S) // 2
        if S[:half] == S[half:]:
            return len(S)

print(solve(S))
