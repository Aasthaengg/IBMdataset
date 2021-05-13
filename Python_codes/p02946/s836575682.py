a, b = map(int, input().split())
ans=[int(x) for x in range(b-a+1,b+a)]
print(*ans)