n = int(input())
s = input()
cnt = 0

for i in range(1,n):
    s1 = s[:i]
    s2 = s[i:]
    cnt = max(cnt, len(list(set(s1) & set(s2))))
    
print(cnt)