k, x = map(int, input().split())

max= x+k-1
min= x-k+1

ans=''
for i in range(min, max+1):
    ans += str(i)+ ' '

print(ans)