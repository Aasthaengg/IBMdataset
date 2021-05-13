
def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())
    a_list = [int(x) - 1 for x in input().rstrip().split(" ")]

    ans = 0
    likes = {i: set() for i in range(n)}
    for i, a in enumerate(a_list):
        if a in likes[i]:
            ans += 1
        likes[a].add(i)

    print(ans)

if __name__ == "__main__":
    resolve()
