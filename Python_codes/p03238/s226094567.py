if int(input()) == 1:
    ans = 'Hello World'
else:
    ans = sum(int(input()) for _ in range(2))
print(ans)
