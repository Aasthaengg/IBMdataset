a,b=map(int, raw_input().split())
ans=b
for i in range(a-1):
    ans=ans*(b-1)
print(ans)