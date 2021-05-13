import sys
input = sys.stdin.readline
def main():
    S = input().rstrip()
    K = int(input())
    if len(set(S)) == 1:
        ans = len(S)*K //2 
        print(ans)
        return
    CNT = 1
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            CNT += 1
        else:
            ans += CNT//2
            CNT = 1
    ans += CNT//2

    if S[0] != S[len(S)-1]:
        print(ans*K)
    else:
        ans2 = 0
        CNT = 1
        SS = S + S
        for i in range(len(SS)-1):
            if SS[i] == SS[i+1]:
                CNT += 1
            else:
                ans2 += CNT//2
                CNT = 1
        ans2 += CNT//2
        # print(ans*(K-1))
        print(ans*K + (ans2-ans*2)*(K-1))

if __name__ == '__main__':
    main()