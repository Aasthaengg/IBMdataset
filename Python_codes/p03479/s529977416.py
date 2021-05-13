x, y = map(int, input().split())

ans = len(format(y//x,'b'))
print(ans)