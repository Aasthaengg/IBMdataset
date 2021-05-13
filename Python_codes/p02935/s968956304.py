N = int(input())
r, *v = sorted(list(map(int, input().split())))
for x in v:
    r = (r+x)/2
print(r)
