from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
write = stdout.write

def main():
    N, M, D = map(int, input().split())

    if not D:
        prob = 1 / N
    else:
        prob = 2 * (N - D) / (N * N)

    ans = prob * (M - 1)
    print(ans)

main()
