s = input()
count = 0
t = len(s)
for i in range(1,t):
    if s[i] != s[i-1]:
        count+=1
print(count)