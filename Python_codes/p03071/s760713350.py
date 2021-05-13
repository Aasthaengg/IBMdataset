a,b = map(int, input().split())
total = max(a,b)
print(total*2 if a == b else total+(total-1))