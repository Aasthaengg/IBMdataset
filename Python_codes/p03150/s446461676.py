s=input()
n=len(s)
for i in range(n):
    for j in range(n):
        if 'keyence'==s[:i]+s[i+j:]:print("YES");exit()
print("NO")