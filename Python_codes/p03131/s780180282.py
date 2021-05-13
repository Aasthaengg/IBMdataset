def main():
    K, A, B = map(int, input().split())
    if A+2 >= B:
        print(K+1)
        return
    ans = A + (B-A)*((K-(A-1))//2) + (K-(A-1))%2
    print(ans)

if __name__ == "__main__":
    main()
