from collections import Counter
INF = 114514191981036436433-4
n = int(input())
s = input()

b = Counter(s)
ans = b["."]

cur = b["."]

for i in range(n):
    if s[i] == "#":
        cur += 1
    else:
        cur -= 1
        
    ans = min(ans,cur)
    
print(ans)