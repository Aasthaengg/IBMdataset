s = input()
n = len(s)//2
count = 0
f = s[:n]   
l = s[-n:]
l = l[::-1]
for i in range(n):
    if f[i] != l[i]:
        count+=1
print(count)