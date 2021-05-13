N = int(input())
aaa = list(map(int, input().split()))
den = 0
for a in aaa:
    den += 1 / a
print(1 / den)
