N = int(input())
ans,a,b,ab = 0,0,0,0

for i in range(N):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A" and s[0] == "B":
        ab += 1
    elif s[-1] == "A":
        a += 1
    elif s[0] == "B":
        b += 1

ans += ab + min(a,b)
if ab > 0 and a == b == 0:
    ans -= 1
print(ans)