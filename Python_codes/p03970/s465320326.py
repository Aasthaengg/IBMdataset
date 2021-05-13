def main():
    S = input()
    ref = "CODEFESTIVAL2016"
    ans = 0

    for i in range(len(S)):
        if ref[i] != S[i]:
            ans += 1

    print(ans)
    
if __name__ == "__main__":
    main()