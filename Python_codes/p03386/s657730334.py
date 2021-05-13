a,b,k = map(int,input().split())
t = []

for i in range(a,a+k):
    if i <= b:
        t.append(i)
for i in range(b-k+1,b+1):
    if i >= a:
        t.append(i)

t = list(set(t))
t.sort()

for i in range(len(t)):
    print(t[i])