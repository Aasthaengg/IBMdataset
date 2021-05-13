def main():
    n, a, b, c, d = map(int, input().split())
    a -= 1; b -= 1; c -= 1; d -= 1;
    s = input()

    if c < d:
        for i in range(a, d-1):
            if s[i:i+2] == "##":
                print("No")
                return 0
        print("Yes")

    else:
        for i in range(a, c-1):
            if s[i:i+2] == "##":
                print("No")
                return 0
        for i in range(b-1, d):
            if s[i:i+3] == "...":
                print("Yes")
                return 0
        print("No")

main()
