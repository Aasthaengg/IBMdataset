n,k=map(int,input().split())
alist=list(map(int,input().split()))

one_count = [0]*41

for a in alist:
    for i,b in enumerate(format(a,'b')[::-1]):
        one_count[i] += int(b)

x = 0
adj = 0
for i,count in enumerate(one_count[::-1]):
    tmp = (count < n/2) * (2**(40-i))
    if x + tmp <= k :
        x += tmp
        adj += (n-2*count) * tmp
print(sum(alist)+adj)