N = int(input())
flag = False
for _ in range(N):
    if int(input()) % 2 != 0:
        flag = True
print("first" if flag else "second")