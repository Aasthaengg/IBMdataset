from sys import stdin
input = stdin.readline

def main():
    N, K = map(int, input().rstrip().split())
    P = list(map(int, input().rstrip().split()))
    P = list(map(lambda x: x -1, P))
    C = list(map(int, input().rstrip().split()))
    ans = -10**18
    for i in range(N):
        x = i
        s = []
        total = 0
        while(True):
            x = P[x]
            s.append(C[x])
            total += C[x]
            if x == i:
                break
        l = len(s)
        t = 0
        for j in range(l):
            t += s[j]
            if j + 1 > K:
                break
            now = t
            if total > 0:
                e = (K - j - 1) // l
                now += total * e
            ans = max(ans, now)
    print(ans)

if __name__ == "__main__":
    main()
    
