import itertools
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    ans = float('inf')
    for i in range(N-1):
        for j in range(i+1, N):
            for k in range(N-1):
                for l in range(k+1, N):
                    cnt = 0
                    for p in range(N):
                        if min(X[i], X[j])<=X[p] and X[p]<=max(X[i], X[j]):
                            if min(Y[k], Y[l])<=Y[p] and Y[p]<=max(Y[k], Y[l]):
                                cnt += 1
                    if cnt>=K:
                        s = abs(X[i]-X[j]) * abs(Y[k]-Y[l])
                        if s!=0:
                            ans = min(ans, s)
    
    print(ans)

if __name__ == '__main__':
    main()