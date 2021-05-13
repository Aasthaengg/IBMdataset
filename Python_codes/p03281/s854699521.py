import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    d =[0] *201

    for i in range(1,201):
        for k in range(1,201):
            if k%i==0 and k%2==1:
                d[k] +=1



    N = int(input())

    print(d[:N+1].count(8))


if __name__ == "__main__":
    main()
