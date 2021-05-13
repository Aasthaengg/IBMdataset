a, b = map(int, input().split())
af = 1
cnt = 0
while af < b:
    af += (a-1)
    cnt += 1
    if af >= b:
        break
print(cnt)
