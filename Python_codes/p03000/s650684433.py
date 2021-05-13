n, x = map(int, input().split())
l = list(map(int, input().split()))
ret = 1
zahyo = 0
for i in l:
    zahyo += i
    if zahyo <= x:
        ret += 1
print(ret)