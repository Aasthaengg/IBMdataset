def main():
    N, A, B, C, D = (int(i) for i in input().split())
    S = "#" + input() + "#"
    if "##" in S[A:C+1] or "##" in S[B:D+1]:
        return print("No")
    if D < C and "..." not in S[B-1:D+2]:
        return print("No")
    print("Yes")


if __name__ == '__main__':
    main()
