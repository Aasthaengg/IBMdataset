import collections

def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    cD = dict(collections.Counter(D))
    cT = dict(collections.Counter(T))

    for k, v in cT.items():
        if k not in cD:
            print("NO")
            exit()
        else:
            if v > cD[k]:
                print("NO")
                exit()

    print("YES")


if __name__ == "__main__":
    main()
