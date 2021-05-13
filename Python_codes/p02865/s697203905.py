def main():
    N = int(input())

    ans = 0
    for i in range(1, N):
        j = N - i

        if i != j:
            ans += 1

    print(ans//2)
    
if __name__ == "__main__":
    main()