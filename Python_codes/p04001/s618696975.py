def solve(S):
    n = len(S) - 1
    result = 0
    for i in range(2**n):
        sum_i = 0
        now = 0
        for j in range(n+1):
            now = now * 10 + int(S[j])
            if j < n:
                if ((i >> j) & 1):
                    sum_i += now
                    now = 0
            else:
                sum_i += now
        result += sum_i
    return result
S = input()
print(solve(S))