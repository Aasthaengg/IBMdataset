n = int(input())
s = str(input())
t = str(input())

if s == t:
    print(n)
    exit()

for i in range(n):
    #print(s[i:], t[:n-1-i+1])
    if s[i:] == t[:n-1-i+1]:
        break
else:
    i = n
    #pass
ans = i*2+(n-i)
print(ans)
