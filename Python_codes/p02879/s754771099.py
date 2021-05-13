a, b = map(int, input().split())

answer = a * b

if a >= 10:
    print(-1)
elif b >= 10:
    print(-1)
else:
    print(answer)