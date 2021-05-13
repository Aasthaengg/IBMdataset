N = int(input())
ans = set()

for _ in range(N):
    a = int(input())
    if not a in ans:
        ans.add(a)
    else:
        ans.remove(a)
print(len(ans))
