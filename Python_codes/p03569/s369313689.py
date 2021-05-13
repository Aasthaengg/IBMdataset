s=input()
s_exit_x=''
ans = 0
for n,i in enumerate(s):
    if i !='x':
        s_exit_x += i
if s_exit_x != s_exit_x[::-1]:
    print(-1)
else:
    left=0
    right=len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -=1
        elif s[left]=="x":
            left += 1
            ans += 1
        else:
            right -=1
            ans += 1
    print(ans)