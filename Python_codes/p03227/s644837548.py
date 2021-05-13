def main():
    S = input()
    if len(S)==2:
        print(S)
    else:
        S = S[2]+S[1]+S[0]
        print(S)

if __name__ == "__main__":
    main()