A,B = map(int,input().split())
if 13<=A:
    ans=B
elif 6<=A:
    ans=B/2
else:
    ans = 0

print(int(ans))