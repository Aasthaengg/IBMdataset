n = int(input())
s = input()
ans = []
first = []
for i in range(n - 2):
    if s[i] in first:continue
    first.append(s[i])
    second = []
    for j in range(i + 1, n - 1):
        if s[j] in second:continue 
        second.append(s[j])
        third = []
        for k in range(j + 1, n):
            if s[k] in third:continue  
            third.append(s[k])
            ans.append(s[i] + s[j] + s[k])
            
print(len(ans))