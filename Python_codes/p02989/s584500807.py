N = int(input())
d = list(sorted(map(int, input().split())))
c = len(d)//2
print(d[c]-d[c-1] if d[c]!=d[c-1] else 0)
