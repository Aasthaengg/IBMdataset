n = int(input())
p = [int(x) for x in input().split()]

cnt=1
saisyouti=p[0]
for i in range(1,n):
    if p[i]<saisyouti:
        cnt+=1
        saisyouti=p[i]

print(cnt)