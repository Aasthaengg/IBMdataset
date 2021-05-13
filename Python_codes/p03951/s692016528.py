n = int(input())
s = input()
t = input()
c = 0
for i in range(1,n+1):
    f = True
    for j in range(i):
        if s[n-i+j]!=t[j]:
            f = False
    if f:c=i
print(n*2-c)
