def main():
    N, A, B, C, D = (int(i) for i in input().split())
    S = input()
    if "##" in S[A:C] or "##" in S[B:D]:
        return print("No")
    if D < C and (S[D-2] == "#" or S[D] == "#"):
        if (S[B-2] == "#" or S[B] == "#") and "..." not in S[B-1:D]:
            return print("No")
    print("Yes")


if __name__ == '__main__':
    main()
