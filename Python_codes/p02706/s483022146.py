# -*- coding: utf-8 -*-

def main():

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sumA = sum(A)

    if sumA > N:
        ans = -1
    
    else:
        ans = N - sumA

    print(ans)


if __name__ == "__main__":
    main()