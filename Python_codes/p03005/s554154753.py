#  --*-coding:utf-8-*--

def f(N, K):
    return N - K if K > 1 else 0



def main():
    N, K  = map(int, input().split())
    print(f(N, K))


if __name__ == '__main__':
    main()
