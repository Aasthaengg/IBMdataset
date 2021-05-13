n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
c = 0
x = []
for i in range(2*(n+1)):
    if c%2==0:
        c+=1
        continue
    val = l[c]
    x.append(val)
    c+=1
x=x[:-1]
print(sum(x))