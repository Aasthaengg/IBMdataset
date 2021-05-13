A, B = map(int, input().split())
Ans = 0
count = 2
while count >= 1:
    if A >= B:
        Ans += A
        A -= 1
    else:
        Ans += B
        B -= 1
    count -= 1

print(Ans)
