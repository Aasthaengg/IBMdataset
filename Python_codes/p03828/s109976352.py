import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    n = int(readline())
    #f(x):=x以下の素数を列挙する関数
    #int -> list
    def f(x):
        if x < 2:
            return [] 
        res = [2]
        for i in range(2, x+1):
            f = True
            for j in res:
                if i%j == 0:
                    f = False
            if f:
                res.append(i)
        return res
    primes = f(n)
    numOfPrime = []
    for p in primes:
        #2^10=1024だから10までで十分
        numOfDiv = 0
        for k in range(1, 11):
            numOfDiv += n//(p**k)
        numOfPrime.append((p, numOfDiv))
    P = int(1e9)+7
    ans = 1
    for i, j in numOfPrime: 
        ans *= (j+1)
        ans %= P
    print(ans) 
if __name__ == '__main__':
    main()
