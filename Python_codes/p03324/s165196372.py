D, N = map(int, input().split())
li = []
cnt = 1
while len(li) < N:
    if cnt % 100 != 0:
        li.append(cnt * 100 ** D)
    cnt += 1

print(li[-1])
