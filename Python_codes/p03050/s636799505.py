class common_function():
    """
        1. よく使いそうで予め用意してあるものをまとめた
        2. よく使いそうな関数群をまとめた
    """
    def make_divisors(self, n:int):
        """
            試し割り法による約数の列挙を行うメソッド
            ある値 n の約数の列挙を行うのに O(n^(1/2)) かかる.
            e.g.
                input: 96
                output: [1, 96, 2, 48, 3, 32, 4, 24, 6, 16, 8, 12]
        """
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        return divisors

def main():
    common = common_function()
    N = int(input())
    m = common.make_divisors(N)
    ans = 0
    for i in m:
        if i == 1:
            continue
        ans += (N%(i-1) == N//(i-1)) * (i-1)
    print(ans)

if __name__ == "__main__":
    main()
