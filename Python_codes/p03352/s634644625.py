def main():
    x = int(input())
    limit = int(x**0.5)+2
    ans = 0
    for i in range(limit):
        for j in range(2,limit):
            p=i**j
            if p <= x:
                ans = max(ans, p)
            else:
                break
    print(ans)

if __name__ == "__main__":
    main()