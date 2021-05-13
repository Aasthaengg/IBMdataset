n = int(input())
d = sorted(list(map(int, input().split())))

m = len(d)//2
print(d[m]-d[m-1])