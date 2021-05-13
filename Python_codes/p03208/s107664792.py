# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n, k = [int(x) for x in input().rstrip().split(" ")]

    h_list = [int(input().rstrip()) for _ in range(n)]
    h_list.sort()
    ans = 1000000000
    for i in range(n - k + 1):

        val = h_list[i+k-1] - h_list[i]
        if val < ans:
            ans = val
    print(ans)


if __name__ == "__main__":
    resolve()
