
def main():
    a, b, c, k = map(int, input().split(" "))
    ans = 0
    ans += min(a,k)
    k = max(k-a-b,0)
    ans -= k
    print(ans)

if __name__ == "__main__":
    main()