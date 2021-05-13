N,X = map(int, input().split())

dis = 0
cnt = 1

for L in map(int, input().split()):
    dis += L
    cnt += dis <= X

print(cnt)