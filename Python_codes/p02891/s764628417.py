import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    K = int(input())
    if S[0] != S[-1]:
        ans = 0
        before = 0
        i = 0
        while i + 1 < len(S):
            while i + 1 < len(S) and S[i] == S[i + 1]:
                i += 1
            ans += (i + 1 - before)//2
            i += 1
            before = i
        print(ans*K)
    else:
        if len(set(S)) == 1:
            print(K*len(S)//2)
        else:
            i = 0
            while i + 1 < len(S) and S[i] == S[i + 1]:
                i += 1
            cut = i + 1
            L = (i + 1)//2
            i += 1
            
            before = i
            R = 0
            while i + 1 < len(S):
                while i + 1 < len(S) and S[i] == S[i + 1]:
                    i += 1
                R += (i + 1 - before)//2
                i += 1
                before = i
            
            S = S[cut:] + S[:cut]
            ans = 0
            before = 0
            i = 0
            while i + 1 < len(S):
                while i + 1 < len(S) and S[i] == S[i + 1]:
                    i += 1
                ans += (i + 1 - before)//2
                i += 1
                before = i
            ans = ans*(K - 1) + R + L
            print(ans)
if __name__ == '__main__':
    main()