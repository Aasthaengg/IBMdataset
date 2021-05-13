n = int(input())
ans = []
start = "a"
stack = []
stack.append(start)
num = ord("a")
while stack:
    v = stack.pop()
    if len(v) == n:
        ans.append(v)
        continue
    s = list(v[::])
    s.sort()
    nex_num = ord(s[-1])
    for i in range(num, nex_num + 2):
        tuika = chr(i)
        stack.append(v + tuika)
print(*ans[::-1], sep="\n")
