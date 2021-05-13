def resolve():
    def is_rotatable(S):
        for i in range(len(S)//2):
            if S[i] != S[-1-i]:
                return False
        return True
    S = input()
    N = len(S)
    if is_rotatable(S) and is_rotatable(S[:N//2]) and is_rotatable(S[(N//2)+1:]):
        print("Yes")
    else:
        print("No")


if '__main__' == __name__:
    resolve()