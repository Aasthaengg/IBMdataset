n = int(input())
ans = []
start = ("a", 1, ord("a"))
stack = []
stack.append(start)
num = ord("a")
while stack:
    v, nagasa, mx = stack.pop()
    if nagasa == n:
        ans.append(v)
        continue
    for i in range(num, mx + 2):
        tuika = chr(i)
        mx = max(i, mx)
        stack.append((v + tuika, nagasa + 1, mx))
print(*ans[::-1], sep="\n")
