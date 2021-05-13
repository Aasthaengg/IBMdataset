n = int(input())
a = list(map(int,input().split()))
neighbor = 1
nei = []
for i in range(1,n):
    if a[i] == a[i-1]:
        neighbor+=1
    else:
        if neighbor >1:
            nei.append(neighbor)
            neighbor = 1
if neighbor >1:
    nei.append(neighbor)
ans = 0
for x in nei:
    ans += x//2 
    
print(ans)