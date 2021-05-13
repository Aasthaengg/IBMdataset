s = input()
a_z = [chr(i) for i in range(97, 97 + 26)]
ans = len(s)
for alp in a_z:
    cnt = 0
    step = 0
    for char in s:
        if char == alp:
            cnt = max(cnt, step)
            step = 0
        else:
            step += 1
    ans = min(max(cnt, step), ans)
print(ans)
