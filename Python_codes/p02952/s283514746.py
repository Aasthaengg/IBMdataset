n = int(input())
cnt = 0
for i in range(n+1):
    if len(str(i)) in {1, 3, 5}:
        cnt += 1
print(cnt -1)