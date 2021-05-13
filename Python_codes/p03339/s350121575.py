n = int(input())
s = input()
l = [0]
ans = 10**6
for i,si in enumerate(s):
    l.append(l[i]+(si=="W"))
for i in range(n):
    ans = min(ans,l[i]+(n-1-i)-(l[-1]-l[i+1]))
    #print(i,f"W{l[i]} E{(n-1-i)-(l[-1]-l[i+1])}",s[:i],s[i+1:])
print(ans)