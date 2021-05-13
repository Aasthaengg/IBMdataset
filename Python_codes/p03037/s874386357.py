# coding: utf-8

def main():
    N, M = map(int, input().split())
    imos = [0] * (N + 2)
    ans = 0

    for _ in range(M):
        l, r = map(int, input().split())
        imos[l] += 1
        imos[r + 1] -= 1

    for i in range(1, N + 2):
        imos[i] += imos[i - 1]
        if imos[i] == M and i != N + 1:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
