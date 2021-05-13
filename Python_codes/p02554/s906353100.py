N = int(input())

ans = 10**N - 2*(9**N) + 8**N
print(ans % 1000000007)
