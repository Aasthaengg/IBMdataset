from collections import defaultdict

def main():
    N,M = map(int, input().split())
    d = defaultdict(lambda: 0)
    A = list(map(int, input().split()))

    for a in A:
        d[a]+=1

    for _ in range(M):
        B,C = map(int, input().split())
        d[C]+=B

    d_sorted = sorted(d.items(), key=lambda x:x[0], reverse=True)
    ans = 0

    for i in range(len(d_sorted)):
        ans += d_sorted[i][0] * min(d_sorted[i][1],N)
        N -= min(d_sorted[i][1],N)
        if N == 0:
            break



    print(ans)







if __name__ == '__main__':
    main()