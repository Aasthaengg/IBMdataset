n = list(input())
m = []
ans = []
for i in range(len(n) - 2):
    s = n[i] + n[i+1] + n[i+2]
    m.append(int(s))
    
for j in m:
    ans.append(abs(753 - j))
    
print(min(ans))