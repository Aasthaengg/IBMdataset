def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    def solve(positive, A):
        total = 0
        ope = 0
        for i in range(len(A)):
            # print("####")
            # print(total)
            # print(ope)
            if positive:
                # 次は負の数=正の数になるなら補正
                if total + A[i] >= 0:
                    ope += total + A[i] + 1
                    total = total + A[i] - (total + A[i]) - 1
                else:
                    total += A[i]
            else:
                # 次は正の数=負の数になるなら補正
                if total + A[i] <= 0:
                    ope += abs(total + A[i]) + 1
                    total = total + A[i] + abs(total + A[i]) + 1
                else:
                    total += A[i]
            positive = (not positive)
        return ope
    
    print(min(solve(True, A), solve(False, A)))



if '__main__' == __name__:
    resolve()