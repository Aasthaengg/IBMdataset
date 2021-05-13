def main():
    A, B, C = input().split()
    if A[-1] == B[0] and B[-1] == C[0]:
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())