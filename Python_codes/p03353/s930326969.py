def main():
    s = input()
    k = int(input())
    ss = set()
    sss = sorted(s)
    for i in range(len(s)):
        for j in range(i+1, i+6):
            ss |= {s[i:j]}
    print(sorted(ss)[k-1])

if __name__ == "__main__":
    main()