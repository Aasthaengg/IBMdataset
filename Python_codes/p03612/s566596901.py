n = int(input())
p = list(map(int, input().split()))
p = [i-1 for i in p]

has_pair = 0
ans = 0
for i in range(n):
    if p[i]==i:
        if has_pair==0:
            has_pair=1
            ans+=1
        else:
            has_pair=0
    else:
        has_pair=0
print(ans)