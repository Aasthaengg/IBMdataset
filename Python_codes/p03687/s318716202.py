s = input()
n = len(s)
char_in_s = set()
for i in range(n):
    char_in_s.add(s[i])
ans = float('inf')
for char in char_in_s:
    max_interval = 0
    now = 0
    for i in range(n-1,-1,-1):
        if s[i] != char:
            now += 1
        else:
            max_interval = max(max_interval,now)
            now = 0
    max_interval = max(max_interval,now)
    ans = min(ans,max_interval)
print(ans)
        
