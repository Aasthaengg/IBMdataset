s = input()
ns = s.replace("x","")
l = len(ns)

if ns[:l//2] == ns[l-1:(l+1)//2-1:-1]:
    ans = 0
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            if s[left] == "x":
                right += 1
            else:
                left -= 1
            ans += 1
        left += 1
        right -= 1
else:
    ans = -1

print(ans)