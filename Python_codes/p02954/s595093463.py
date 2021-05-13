s = list(input())
ans = [0]*len(s)

i = 0
while i != len(s):
    cnt1 = 0
    cnt2 = 0
    while s[i + cnt1] == "R":
        cnt1 += 1
    ans[i + cnt1] += cnt1//2
    ans[i + cnt1 - 1] += cnt1//2 + cnt1%2
    while s[i + cnt1 + cnt2] == "L":
        cnt2 += 1
        if i + cnt1 + cnt2 == len(s):
            break
    ans[i + cnt1] += cnt2//2 + cnt2%2
    ans[i + cnt1 - 1] += cnt2//2
    i += cnt1 + cnt2

an = [str(i) for i in ans]
print(" ".join(an))