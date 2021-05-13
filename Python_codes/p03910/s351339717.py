n = int(input())
ans = []
cnt = 0
for i in range(1, int(n**0.7)+3):
    if n > cnt:
        ans.append(i)
        cnt += i
    else:
        if cnt - n in ans:
            ans.remove(cnt - n)
        break
for i in ans:
    print(i)