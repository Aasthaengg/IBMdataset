import sys

readline = sys.stdin.readline


def main():
    N = int(readline())
    cnt = 0; leftB = 0; rightA = 0; same = 0
    for _ in range(N):
        s = readline()[:-1]
        for i in range(len(s)-1):
            subs = s[i:i+2]
            cnt += subs == 'AB'
        leftB += s[0] == 'B'
        rightA += s[-1] == 'A'
        same += s[0] == 'B' and s[-1] == 'A'
    
    if same == leftB == rightA:
        ans = cnt + max(min(N-1, same-1), 0)
    else:
        ans = cnt + min(N-1, leftB, rightA)
    print(ans)

if __name__ == "__main__":
    main()
