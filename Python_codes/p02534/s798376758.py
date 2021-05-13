import sys


def resolve(in_):
    K = int(next(in_))
    return 'ACL' * K
    

def main():
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()
