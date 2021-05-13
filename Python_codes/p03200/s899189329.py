def main():
    S = input()
    ans = 0
    wc = 0

    for i in range(len(S)):
        if S[i] == "W":
            ans += i - wc
            wc += 1
            
    print(ans)

if __name__ == "__main__":
    main()