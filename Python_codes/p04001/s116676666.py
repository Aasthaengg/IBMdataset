import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    ans = 0
    S = SI()
    bit_len = len(S)-1
    for i in range(2**bit_len):
        ls = ["" for _ in range(bit_len)]
        for j in range(bit_len):
            if (i >> j) & 1:
                ls[j] = "+"
                
        calc = []
        for n in range(len(S)):
            calc.append(S[n])
            if n != len(S)-1:
                calc.append(ls[n])
        ans += eval("".join(calc))
    print(ans)

if __name__ == '__main__':
    main()