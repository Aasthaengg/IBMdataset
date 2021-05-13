s = input()
ans = 0
cnt = 0

for i in range(len(s)):
    if s[i] in ("A", "C", "G", "T"):
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0
if cnt > ans:
    ans = cnt
print (ans) 
