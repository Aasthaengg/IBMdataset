N = int(input())
s = [int(input()) for i in range(N)]

s.sort()

ans = sum(s)
for i in range(N):
    if ans%10 != 0:
        break
    elif s[i]%10 != 0:
        ans -= s[i]

print(ans if ans%10!=0 else 0)