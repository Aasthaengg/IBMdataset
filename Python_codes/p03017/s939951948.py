n,a,b,c,d = [int(x) for x in input().split()]
s = input()

ans = "Yes"
if c > d:
    tmp = s[b-2:d+1].count("...")
    if tmp == 0:
        ans = "No"

tmp = s[a-1:max(c,d)].count("##")
if tmp > 0:
    ans = "No"
print(ans)