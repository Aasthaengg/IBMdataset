all = int(input())
cake = int(input())
donut = int(input())

all -= cake
#ans = donut / all
ans = all % donut
print(ans)