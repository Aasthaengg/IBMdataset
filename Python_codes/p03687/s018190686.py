s = input()

if len(set(s)) == len(s):
    print(len(s)//2)
    exit()

ans = len(s)
for ml in [chr(i) for i in range(ord('a'), ord('z')+1)]:
    tmp = -1
    tmp_ans = 0
    for i in range(len(s)):
        if s[i] == ml:
            tmp_ans = max(tmp_ans, i - tmp - 1)
            tmp = i
    tmp_ans = max(tmp_ans, len(s) - tmp - 1)
    ans = min(ans, tmp_ans)

print(ans)