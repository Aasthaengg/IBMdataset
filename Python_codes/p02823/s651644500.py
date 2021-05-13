def main():
    n, a, b = map(int, input().split())
    if (b-a) % 2 == 0:
        print((b-a)//2)
    else:
        temp = [(min(n-a, b-1))]

        cnt1 = 0
        cnt2 = 0
        for i in range(0, (min(n-a, b-1))):
            if (b-(a-1) - i) % 2 == 0 and cnt1 == 0:
                temp.append(a - 1 + i + (b-(a-1) - i) // 2)
                cnt1 += 1
            elif (n - (a+(n-b)+i)) % 2 == 0 and cnt2 == 0:
                temp.append(n - b + i + (n - (a+(n-b)+i)) // 2)
                cnt2 += 1

            if cnt1 == 1 and cnt2 == 1:
                break

        print(min(temp))

if __name__ == "__main__":
    main()