def main():
    N, Q = map(int, input().split())
    S = input()

    count = [0 for i in range(N + 1)]
    c = 0
    for i in range(1, N):
        if S[i-1] == "A" and S[i] == "C":
            c += 1
        count[i + 1] = c
    
    Query = list()
    for q in range(Q):
        Query.append(input())

    for q in range(Q):
        l, r = map(int, Query[q].split())
        print(count[r] - count[l])

if __name__ == "__main__":
    main()