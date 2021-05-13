k, t = map(int, input().split())
a = sorted(list(map(int, input().split())))

print(max(a[-1]-1-(sum(a)-a[-1]), 0))