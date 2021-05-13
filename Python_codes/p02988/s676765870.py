n = int(input())
p = [int(i) for i in input().split()]
ans = 0
for i in range(1,n) :
    ix = p[i-1:i+2]
    if min(ix) != ix[1] and max(ix)!= ix[1] :
        ans += 1
#        print(ix)
print(ans)