s = input()[::-1]
ls = ['dream', 'dreamer', 'erase', 'eraser']
ls = [ls[i][::-1] for i in range(4)]
ans = 'YES'
i = 0
while i < len(s):
    ng = 1
    for j in range(4):
        if s[i:i+len(ls[j])] == ls[j]:
            i += len(ls[j])
            ng = 0
    if ng:
        ans = 'NO'
        break
print(ans)