n = int(input())

ans = False

for _ in range(n):
    if int(input())%2 == 1:
        ans = True

print("first" if ans else "second")