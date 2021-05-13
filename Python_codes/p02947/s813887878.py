from collections import Counter
 
n = int(input())
s = [list(input()) for _ in range(n)]
for i in range(n):
    s[i].sort()
    s[i] = ''.join(s[i])
counter = Counter(s)
#print(counter)
ans = 0
for val in counter.values():
    #countC2
    ans += val*(val-1)//2
    
print(ans)