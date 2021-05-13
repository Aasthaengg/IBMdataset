def solve(S):
    N = len(S) - 1
    ret = 0
    used_equation = set()
    for i in range(pow(2, N)):
        tmp_equation = ''
        last_j = -1
        for j in range(N):
            if i >> j & 1:
                tmp_equation = tmp_equation + '+' + S[last_j + 1: j + 1]
                last_j = j
        if last_j < N:
            tmp_equation = tmp_equation + '+' + S[last_j + 1:]
        ret += eval(tmp_equation) if tmp_equation not in used_equation else 0
        used_equation.add(tmp_equation)
    print(ret)

if __name__ == "__main__":
    S = input()
    solve(S)