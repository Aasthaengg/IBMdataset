from collections import defaultdict

def main():
    N = list(map(int, input().split()))
    dd = defaultdict(int)

    for n in range(len(N)):
        dd[N[n]] += 1

    print('Yes') if len(dd) == 2 else print('No')

if __name__ == '__main__':
    main()
