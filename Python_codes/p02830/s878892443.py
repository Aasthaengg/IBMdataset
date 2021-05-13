n = int(input())
s, t = input().split()
print(*[si + ti for si, ti in zip(s, t)], sep='')