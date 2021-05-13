n = int(input())
l = [2,1]
if n>=2:
    for i in range(n-1):
        l.append(l[i]+l[i+1])
print(l[-1])