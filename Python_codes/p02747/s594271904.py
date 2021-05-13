def main():
    S = input()
    if len(S) % 2 == 1:
        print("No")
        return
    for i in range(0, len(S), 2):
        if S[i:i+2] != "hi":
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
