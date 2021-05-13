
def resolve():
    import sys
    import string
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n, k, q = [int(x) for x in input().rstrip().split(" ")]

    scores = [k - q for _ in range(n)]

    for i in range(q):
        a = int(input().rstrip())
        scores[a-1] += 1


    for score in scores:
        if score <= 0:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    resolve()
