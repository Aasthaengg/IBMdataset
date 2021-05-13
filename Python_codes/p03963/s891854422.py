# B - AtCoDeerくんとボール色塗り
def main():
    n, k = map(int,input().split())

    for i in range(n):
        if i == 0:
            val = k
        else:
            val *= (k-1)
    else:
        print(val)


if __name__ ==  "__main__":
    main()