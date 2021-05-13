from math import ceil
def main():
    N = int(input())
    if N%2==1:
        print(0)
        return
    else:
        # N=k*5^xのxが答えとする
        ans = 0
        N //= 2
        while N:
            ans += N//5
            N //= 5
        print(ans)
        return


main()
