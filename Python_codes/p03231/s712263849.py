import math

class common_function():
    """
        1. よく使いそうで予め用意しておいた変数をまとめた
        2. よく使いそうな関数群をまとめた
    """
    def lcm(self, x:int, y:int):
        """
            最小公倍数を返すメソッド
            math をインポートする
        """
        return (x * y) // math.gcd(x, y)
        

def main():
    common = common_function()
    N, M = map(int, input().split())
    S = input()
    T = input()
    lengthX = common.lcm(N, M)
    XdivS = lengthX//N
    XdivT = lengthX//M
    X = []
    for i in range(N):
        j = XdivS*i
        X.append((j, S[i]))
    X.sort(key=lambda x: x[0], reverse=True)
    
    k, x = X.pop()
    for i in range(M):
        j = XdivT*i
        for a in range(lengthX):
            if len(X) == 0:
                break
            if k < j:
                k, x = X.pop()
            else:
                break
        if k == j:
            if x != T[i]:
                print(-1)
                return
    print(lengthX)

if __name__ == "__main__":
    main()
