n,k = map(int,input().split())
l = [-1]+list(map(int,input().split()))

visited = [-1]+[False]*n

i = 1
while True:
    if visited[i]:
        fragrant = i
        break
    else:
        visited[i] = True
        i = l[i]

i = fragrant
cnt = 1
while l[i] != fragrant:
    cnt += 1
    i = l[i]
# print(cnt)

i = 1
while k > 0:
    i = l[i]
    k -= 1
    if i == fragrant:
        k %= cnt
print(i)