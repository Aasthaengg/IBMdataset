import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = n * (n + 1) // 2
    n_3 = n // 3
    n_5 = n // 5
    n_15 = n // 15
    ans -= n_3 * (n_3 + 1) * 3 // 2
    ans -= n_5 * (n_5 + 1) * 5 // 2
    ans += n_15 * (n_15 + 1) * 15 // 2
    print(ans)

main()