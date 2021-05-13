S = input().strip()

ans = [""]
prev = ""
for i, s in enumerate(S):
    prev += s
    if ans[-1] != prev:
        ans.append(prev)
        prev = ""
    else:
        if i == len(S) - 1:
            ans.append(prev)

result = len(ans) - 1
if ans[-1] == ans[-2]:
    result -= 1

print(result)


