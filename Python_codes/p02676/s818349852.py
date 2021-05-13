K = int(input())
S = input()
def result(K: int, S: str) -> str:
    s_len = len(S)
    if s_len <= K:
        return S
    else:
        answer = ''
        i = 0
        while i <= K-1:
            answer += S[i]
            i += 1
        answer += '...'
        return answer
print(result(K, S))
