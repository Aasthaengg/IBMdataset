def solve():
    A, B, K = list(map(int, input().split()))
    common_div = []
    for i in range(1, min(A, B)+1):
        if(A % i == 0 and B % i == 0):
            common_div.append(i)
    common_div.sort(reverse=True)
    print(common_div[K-1])


if __name__ == "__main__":
    solve()