def main():
    S = input().strip()
    aa = False
    for i in range(len(S)-1):
        if S[i] == "A" and S[i+1] == "A":
            aa = True
            break
    if not aa:
        if "KIH" in S:
            tmp = S.replace("A", "")
            if tmp == "KIHBR":
                print("YES")
                return
    print("NO")
    return



if __name__ == "__main__":
    main()
