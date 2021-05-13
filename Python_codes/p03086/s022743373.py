a =['A','C','G','T']
s = list(input())
cnt = 0
ans = cnt

for i in s:
    if a.count(i):
        cnt += 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 0

print(ans)