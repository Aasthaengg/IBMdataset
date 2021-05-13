N = int(input())

div = 10**9 + 7

ans = ((10**N) - ((2 * (9**N)) - (8**N))) % div

print(ans)