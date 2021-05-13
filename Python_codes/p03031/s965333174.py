import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N, M = NMI()
    KS = [NLI() for _ in range(M)]
    P = NLI()
    
    ans = 0
    
    for m in range(M):
        for x in range(1,len(KS[m])):
            KS[m][x] -= 1

    bit_len = N
    for i in range(2**bit_len):
        switch = [0 for _ in range(bit_len)]
        for j in range(bit_len):
            if (i >> j) & 1:
                switch[j] = 1
        
        light = [0 for _ in range(M)]
        
        for m in range(M):
            cnt = 0
            for y in KS[m][1:]:
                if switch[y] == 1:
                    cnt += 1
            if cnt % 2 == P[m]:
                light[m] = 1
        
        if light.count(1) == M:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()