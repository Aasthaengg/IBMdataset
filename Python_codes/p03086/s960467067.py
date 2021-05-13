n = input()
cnt = 0
ans = 0
for i in range(len(n)):
    if n[i] in "ACGT":
        cnt += 1
        if ans <= cnt:
            ans = cnt
    else:
        cnt = 0
print(ans)