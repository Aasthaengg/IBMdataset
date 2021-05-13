import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    S = list(input()[:-1])
    ans = 0; rtmp = 0
    cnt = K + (S[0] == '1')
    for l in range(N):
        if cnt > 0:
            for r in range(rtmp, N):
                if r == N-1:
                    break
                if S[r] > S[r+1]:
                    cnt -= 1
                if cnt <= 0:
                    break
        rtmp = r+1
        ans = max(rtmp - l, ans)
        if l == N-1:
            break
        if S[l] < S[l+1]:
            cnt += 1

    print(ans)
    
if __name__ == "__main__":
    main()
