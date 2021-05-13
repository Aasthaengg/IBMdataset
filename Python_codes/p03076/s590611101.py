a = list(int(input()) for _ in range(5))
b = list(map(lambda x: (10-x%10)%10, a))

ans = sum(a)+sum(b)-max(b)
print(ans)