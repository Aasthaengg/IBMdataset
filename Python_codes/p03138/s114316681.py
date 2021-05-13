import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 0:
        print(sum(A))
        return
    
    bitK = bin(K)[2:]
    l = len(bitK)
    tight = True
    X = 0
    for n in range(l):
        one_num = 0
        for a in A:
            if a & (1 << (l - 1 - n)): one_num += 1
        if one_num > N - one_num: # Xの(n-1-i)ビット目は0推奨
            if bitK[n] == "1":
                tight = False
                X = X * 2
            else:
                X = X * 2
        elif one_num < N - one_num: # Xの(n-1-i)ビット目は1推奨
            if bitK[n] == "1":
                X = X * 2 + 1
            elif tight:
                X = X * 2
            else:
                X = X * 2 + 1
        else: # Xの(n-1-i)ビット目はどちらでもよい
            if bitK[n] == "1":
                tight = False
                X = X * 2
            else:
                X = X * 2
    ans = 0
    for a in A: ans += X ^ a
    #print(X)
    print(ans)



if __name__ == "__main__":
    main()
