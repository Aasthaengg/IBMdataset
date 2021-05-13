a,b,c = sorted(list(map(int, input().split())))
# 同じ数が2つできるまで、小さい2つの数に１を足す
ans=0
if b!=c:
    b+=ans
    ans+=c-b
a+=ans
q,r = divmod(c-a, 2)
ans+=q
if r>0:
    ans+=2
print(ans)