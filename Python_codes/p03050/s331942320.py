n = int(input())
ans = 0
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        if i>1 and n//(i-1)==n%(i-1):
            ans += i-1
        if n//i>1 and n//(n//i-1)==n%(n//i-1):
            ans += n//i-1
print(ans)