a,b,c = list(map(int,input().split()))
ans_a = min(b,c)
if b+c > a:
    ans_b = b+c-a
else:
    ans_b = 0
print(ans_a,ans_b)