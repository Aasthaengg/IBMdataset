n = int(input())
a_list = [int(input()) - 1 for _ in range(n)]
s = set()
i = 0
ans = -1
while i not in s:
    if i == 1:
        ans = len(s)
        break
    s.add(i)
    i = a_list[i]
print(ans)