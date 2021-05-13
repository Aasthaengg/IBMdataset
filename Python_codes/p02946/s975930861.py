K,X=map(int,input().split())
ans_p=ans_n=X

for _ in range(K-1):
    ans_p+=1
    ans_n-=1

print(*[x for x in range(ans_n,ans_p+1)])

