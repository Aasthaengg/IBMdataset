n = int(input())
s = list(map(int,input().split()))
c = 0
for i in range(n-2):
    if s[i+1] != min(s[i],s[i+1],s[i+2]) and s[i+1] != max(s[i],s[i+1],s[i+2]):
        c += 1
print(c)