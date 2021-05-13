
def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    MOD = 10**9 + 7
    MAX_N = 10**5

    count_arr = [0]*(MAX_N+1)
    count_arr[0] = 3

    ans = 1
    for a in A:
        ans *= count_arr[a]
        ans %= MOD

        count_arr[a] -= 1
        count_arr[a+1] += 1

    print(ans)

if __name__ == "__main__":
    main()