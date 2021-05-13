a,b,k = map(int, input().split())
li = dict(a = a, b = b, k = k)

now = "a"
for i in range(li["k"]):
    add = 0
    if li[now] % 2:
        li[now] -= 1
    li[now] = int(li[now]/2)
    add += li[now]
    if now == "a":
        now = "b"
    else:
        now = "a"
    li[now] += add
print(li["a"],li["b"])