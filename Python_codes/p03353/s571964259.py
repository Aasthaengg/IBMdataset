s = input()
k = int(input())
x = []
n = len(s)
for i in range(k):
    for j in range(n-i):
        t = s[j:j+i+1]
        if not t in x:
            x.append(t)
x.sort()
print(x[k-1])