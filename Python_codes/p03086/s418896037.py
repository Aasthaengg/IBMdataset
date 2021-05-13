S = input()
cnt = ans = 0
for s in S:
    if s in ["A","T","G","C"]:
        cnt += 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 0
print(ans)