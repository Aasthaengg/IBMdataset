s = str(input())
n = int(input())
k = ord("z")
a = [0]*len(s)
for i in range(len(s)):
    a[i] = ord(s[i])
for i in range(len(s)):
    if a[i] == ord("a"):
        continue
    if n>=k+1-a[i]:
        n = n-k-1+a[i]
        a[i] = ord("a")
    
    if n<=0:
        break
if n>0:
    a[-1] += n%26
ans = ""
for i in range(len(s)):
    ans += chr(a[i])
print(ans)
