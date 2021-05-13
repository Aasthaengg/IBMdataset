def main():
    N = input()
    lenN = len(N)
    listN = list(N)
    N2 = [int(i) for i in listN]
    bf = sum(N2)
    ans = 0
    for i, s in enumerate(N):            
        if s == '9':
           ans += 9
        else:
            if i == 0:
                ans += int(s)-1 + 9*(lenN - i - 1)
                break
            else:
                ans += 9*(lenN - i) - 1
                break
    ans = max(ans, bf)
    print(ans)

if __name__ == "__main__":
    main()
