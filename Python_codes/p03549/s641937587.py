import collections
def main():
    n,m=map(int, input().split())

    correct = (n-m)*100
    wrong = m*1900

    res = 0

    k = 2**m

    print(k*(correct+wrong))

    



if __name__ == '__main__':
    main()
