k,s=map(int,input().split())
cnt=0

for i in range(k+1):
    if i <= s:
        for j in range(k+1):
            if i+j<=s:
                if 0<=s-i-j<=k:
                    cnt+=1
print(cnt)
