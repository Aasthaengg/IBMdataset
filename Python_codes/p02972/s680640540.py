import math
import collections

def main():
    n = int(input())
    a=[int(i) for i in input().split()]

    #0 < i < N+1 の iについて、iの倍数が書かれた箱に入ってるボールの個数を2で割った余りがai
    # 1 <= N < 2*10**5
    good = [0]*(n+1)
    for i in range(n//2+1,n+1):
        good[i] = a[i-1]
    for i in range(n//2,0,-1):
        tmp = 0
        odd_even = a[i-1]
        for j in range(i+i,n+1,i):
            tmp += good[j]
        if(odd_even!=tmp%2):
            good[i] = 1

    print(sum(good))

    for i in range(1,n+1):
        if(good[i]):
            print(i,end=" ")
    print()

if __name__ == '__main__':
    main()
