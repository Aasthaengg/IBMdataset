import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def main():
    N = int(input())
    c = list(input())[:-1]
    # bad_pairs = []
    w_count = 0
    r_count = 0
    for i in range(N):
        if c[i] == 'W':
            w_count += 1
        else:
            r_count += 1
        # if c[i] == 'W' and i < N - 1 and c[i + 1] == 'R':
        #     bad_pairs.append({ 'W': i, 'R': i + 1 })
    # if len(bad_pairs) == 0:
    #     print(0)
    #     exit(0)
    if w_count == N or r_count == N:
        print(0)
        exit(0)
    no_exchange = 0
    for i in range(r_count):
        if c[i] == 'R':
            no_exchange += 1
    # print(no_exchange, w_count, r_count)
    print(r_count - no_exchange)

if __name__ == '__main__':
    main()
