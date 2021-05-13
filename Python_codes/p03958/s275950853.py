k, t = map(int, input().split())
aaa = list(map(int, input().split()))
m = max(aaa)
if m <= (k + 1) // 2:
    print(0)
    exit()

others = k - m
print(k - (others * 2 + 1))
