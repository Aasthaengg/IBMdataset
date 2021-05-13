N,A,B,C,D = map(int, input().split())
S = [""] + list(input()) + [""]

def can(start, end):
    for i in range(start, end):
        if S[i] == S[i + 1] == "#":
            return False
    return True

def main():
    if not (can(A, C) and can(B, D)):
        return False

    if C < D:
        return True
    elif C > D:
        for i in range(B, D + 1):
            if S[i - 1] == S[i] == S[i + 1] == ".":
                return True
        return False

if __name__ == "__main__":
    if main():
        print('Yes')
    else:
        print('No')