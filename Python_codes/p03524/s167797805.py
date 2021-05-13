s=list(input())

a=s.count("a")
b=s.count("b")
c=len(s)-a-b

M=max(a, b, c)-min(a, b, c)

if M<=1:
    print("YES")
else:
    print("NO")