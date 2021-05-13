h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
colors = []
ans = [[None] * w for _ in range(h)]
dir = True

for i in range(len(a)):
    num = int(a[i])
    for j in range(num):
        colors.append(i+1)

#print(colors)

for i in range(h):
    if dir:
        for j in range(w):
            num = colors[0]
            ans[i][j] = num
            del colors[0]
        dir = not dir
    else:
        for j in reversed(range(w)):
            num = colors[0]
            ans[i][j] = num
            del colors[0]
        dir = not dir

#print(ans)

for i in range(len(ans)):
    print(*ans[i])


'''
3 5
5
1 2 3 4 5
'''