def main():
    A, B, C, D = map(int, input().split())
    S1 = A*B
    S2 = C*D

    if S1 > S2:
        print(S1)
    elif S1 < S2:
        print(S2)
    else:
        print(S1)
main()