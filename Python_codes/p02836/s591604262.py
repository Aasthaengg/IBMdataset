s=input()
s_rev = s[::-1]
count = 0
for i in range(len(s)):
    if s[i] != s_rev[i]:
        
        count += 1
if count %2 == 0  :
    count /= 2
print(int(count))