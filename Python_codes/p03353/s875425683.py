def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = set()
    for i in range(n):
        for j in range(i+1, i+k+1):
           ans |= {s[i:j]}
    print(list(sorted(ans))[k-1])

if __name__ == "__main__":
    main()