month, day = map(int, input().split())

ans = month-1 if month > day else month

print(ans)
