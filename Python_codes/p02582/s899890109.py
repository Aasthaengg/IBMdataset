w = list(input())
out = 0
cnt = 0
for i in range(len(w)):
    if w[i] == "S":
        cnt = 0
    elif w[i] == "R":
        cnt += 1
        out = max(out, cnt)
print(out)