n = int(input())
li = list(map(int,input().split()))
ma = max(li)
li.remove(ma)
diff = []
for l in li:

    diff.append(abs(ma/2-l))
mi = min(diff)
ind = diff.index(mi)
print(ma,li[ind])