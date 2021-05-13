n,k = map(int,input().split())
s = input()
a = []
c = 1
for i in range(n-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        a.append(c)
        c = 1
a.append(c)
b = [0]
for i in range(len(a)):
    b.append(b[-1]+a[i])
b.append(b[-1])
n = len(b)
l = 2*k+1
st=int(s[0])
ans = 0
for i in range(st,n,2):
    ans = max(ans,b[i]-b[max(0,i-l)])
print(ans)
