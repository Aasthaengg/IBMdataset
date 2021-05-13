a = sorted(list(map(int, input().split())))
k = int(input())

print(sum(a[:2])+a[-1]*2**k)
