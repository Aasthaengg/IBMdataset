import sys
input = sys.stdin.readline


def main():
    S = input().rstrip()
    K = int(input())

    N = len(S)
    if S == S[0] * N:
        ans = (N * K) // 2
    elif S[0] == S[-1]:
        a = 1
        for i in range(N):
            if S[i] == S[i+1]:
                a += 1
            else:
                break
        b = 1
        for i in reversed(range(N)):
            if S[i-1] == S[i]:
                b += 1
            else:
                break
        seq = 1
        ans = 0
        for i in range(a, N-b):
            if S[i] == S[i+1]:
                seq += 1
            elif seq > 1:
                ans += seq//2
                seq = 1
        if seq > 1:
            ans += seq//2
        ans *= K
        ans += a//2
        ans += (a+b)//2 * (K-1)
        ans += b//2
    else:
        seq = 1
        ans = 0
        for i in range(N-1):
            if S[i] == S[i+1]:
                seq += 1
            elif seq > 1:
                ans += seq//2
                seq = 1
        if seq > 1:
            ans += seq//2
        ans *= K

    print(ans)


if __name__ == "__main__":
    main()
