s = str(input())
k = int(input())
a = []
for i in range(len(s)):
    for j in range(1,k+1):
        if i+j>len(s):
            break
        a.append(s[i:i+j])
a = list(set(a))
a.sort()
print(a[k-1])