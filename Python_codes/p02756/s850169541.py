s = list(input())
q = int(input())
r = 0
first = []
last = []

for i in range(q):
    query = list(input().split())

    if query[0] == "1":
        r = (r+1) % 2
        continue

    if r == 0:
        if query[1] == "1":
            first.append(query[2])
        else:
            last.append(query[2])
    else:
        if query[1] == "1":
            last.append(query[2])
        else:
            first.append(query[2])

first.reverse()
ans = first + s + last

if r == 1:
    ans.reverse()

print("".join(ans))