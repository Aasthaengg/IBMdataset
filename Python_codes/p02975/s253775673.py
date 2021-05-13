n = int(input())
a = sorted(list(map(int, input().split())))
c0 = a.count(0)

ans = "No"
if c0==n: ans = "Yes"
elif len(set(a)) == 2:
    c = a.count(a[-1])
    if c == (2*n)//3 and c0 == n//3: ans = "Yes"
elif len(set(a)) == 3:
    x,y,z = list(set(a))
    if a.count(x) == a.count(y) == a.count(z):
        if int(bin(x ^ y ^ z),2) == 0: ans = "Yes"
print(ans)