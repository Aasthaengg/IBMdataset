n,k = map(int,input().split())
s = input()
x = len(s)
lst = [0]
ans = 0
if s[0] == "1" and s[x-1] == "0":
    s = s[::-1]
for i in range(1,x):
    if s[i-1] != s[i]:
        lst.append(i)
lst.append(x)
if s[0] == "0" and s[x-1] == "1":
    if 2*k >= len(lst):
        ans = x
    else:
        i = 1
        while i+2*k+1 <= len(lst)-1:
            ans = max(ans,lst[i+2*k+1]-lst[i])
            i += 2
        ans = max(ans,lst[2*k])
if s[0] == "0" and s[x-1] == "0":
    if 2*k >= len(lst):
        ans = x
    else:
        i = 1
        while i+2*k+1 <= len(lst)-1:
            ans = max(ans,lst[i+2*k+1]-lst[i])
            i += 2
        ans = max(ans,lst[2*k])
        ans = max(ans,x-lst[len(lst)-2*k-1])
if s[0] == "1" and s[x-1] == "1":
    if 2*k+1 >= len(lst):
        ans = x
    else:
        i = 0
        while i+2*k+1 <= len(lst)-1:
            ans = max(ans,lst[i+2*k+1]-lst[i])
            i += 2
print(ans)