from collections import defaultdict

def main():
    n, k, q = map(int, input().split(" "))
    a = (int(input()) for i in range(q))
    d = defaultdict(lambda:k-q)
    for i in range(n):
        d[i]

    for i in a:
        d[i-1] += 1

    for value in d.values():
        print("Yes" if value > 0 else "No")


main()