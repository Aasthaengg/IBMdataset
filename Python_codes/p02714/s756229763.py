def solve():
    N = int(input())
    S = input()
    cnt = {}
    for c in S:
        cnt[c] = cnt.get(c, 0) + 1
    total_triplets = cnt.get('R', 0) * cnt.get('G', 0) * cnt.get('B', 0)
    for stride in range(1, N):
        for i in range(0, N-2*stride):
            j = i + stride
            k = j + stride
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                total_triplets -= 1
    print(total_triplets)

if __name__ == "__main__":
    solve()