n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

li = []
sumb = 0
for a,b in ab:
    li.append(a+b)
    sumb += b

li.sort(reverse = True)


print(sum(li[::2]) - sumb)
