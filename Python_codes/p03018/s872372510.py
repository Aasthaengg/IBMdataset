s = list(input())[::-1]+["L"]
n = len(s)

ans = 0
count = 0
now = 0
while now < n-1:
    if s[now] == "C" and s[now+1] == "B":
        count += 1
        now += 2
    elif s[now] == "A":
        if count > 0:
            ans += count
        else:
            count = 0
        now += 1
    else:
        count = 0
        now += 1
print(ans)