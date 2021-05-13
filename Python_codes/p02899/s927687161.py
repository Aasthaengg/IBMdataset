N = int(input())
aaa = list(map(int, input().split()))
x = [(a, i) for i, a in enumerate(aaa, 1)]
x.sort()
ans = []
for a, i in x:
    ans.append(i)
print(*ans)
