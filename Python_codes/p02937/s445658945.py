import bisect
s = list(input())
t = list(input())
ls = len(s)
check = [[] for i in range(26)]
for i in range(len(s)):
    o = ord(s[i])-ord("a")

    check[o].append(i+1)
ans = 0
c1 = 0

for i in t:
    o =ord(i)-ord("a")
    if check[o]:
        x = bisect.bisect_right(check[o],ans) 
        if x == len(check[o]):
            c1 += 1
            ans = check[o][0]
        else:
            ans = check[o][x]
            

    else:
        print(-1)
        exit()
 
print(ans+c1*ls)
