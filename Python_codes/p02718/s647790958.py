n,m = map(int,input().split())
a = list(map(int,input().split()))
count = 0
for i in a:
    if sum(a)/(4*m) <= i:
        count+=1
print('Yes' if count >= m else 'No')