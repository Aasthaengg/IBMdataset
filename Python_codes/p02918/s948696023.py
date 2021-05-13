def main():
    N, K = map(int, input().split())
    S = input()
    score = 0
    for i in range(1, N):
        if S[i-1] == S[i]:
            score += 1
    print(min(N-1, score + 2*K))
main()