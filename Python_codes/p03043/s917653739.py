def main():
    import math
    n, k = map(int,input().split())
    kakuritsu = 0
    for i in range(1, n+1):
        kaisuu = math.ceil(math.log2(k/i))
        if i > k:
            kakuritsu += 1/n
        else:
            kakuritsu += (1/n) * ((1/2) ** kaisuu)
    print(kakuritsu)



if __name__ == "__main__":
    main()