s = input()
k = int(input())
n = len(s)
t = set()
for i in range(k):
    for j in range(n-i):
        t.add(s[j:j+i+1])
lis = sorted(list(t))
print(lis[k-1])
