value, money, max_count = map(int, input().split())

ans = min(money // value, max_count)
print(ans)