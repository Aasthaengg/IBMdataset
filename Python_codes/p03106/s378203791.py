a,b,k = map(int,input().split())
lst = []
end = min(a,b) #実際の終わり

for i in range(1,end+1):
    ra = a % i
    rb = b % i
    if ra == 0 and rb == 0:
        lst.append(i)

ans = lst[-1*k]
print(ans)