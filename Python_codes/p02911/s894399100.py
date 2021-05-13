from collections import defaultdict

def main():
    N, K, Q = map(int,input().split())
    cnt = defaultdict(int)

    for _ in range(Q):
        a = int(input())
        cnt[a] += 1

    for n in range(1, N+1):
        score = K - Q + cnt[n]

        if score > 0:
            print("Yes")
        else:
            print("No")
    

if __name__ == "__main__":
    main()

