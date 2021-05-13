
def check(i, j, k, K):
    if (i + j + 2) % K == 0 and (i + k + 2) % K == 0 and (k + j + 2) % K == 0:
        return 1
    else:
        return 0


def get_num(i, j, k):
    if i != j and i != k and j != k:
        return 6
    elif i == j == k:
        return 1
    else:
        return 3

def main():
    a, b = map(int, input().split())
    print(a - b + 1)

if __name__ == '__main__':
    main()
