n = int(input())
ans = 0
s = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a,b,c = s[i],s[j],s[k]
            if a != b!= c!= a and a+b >c and a+c >b and c+b >a:ans +=1
print(ans)
