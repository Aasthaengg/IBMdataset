k = int(input())
q = (k-1)//50
s = (k-1)%50+1
ans = [0]*50
if k == 0:
    pass
elif k<50:
    for i in range(50):
        if i<s:
            ans[i] = 50
        else:
            ans[i] = 0
else:
    for i in range(50):
        if i<s:
            ans[i] = q+50
        else:
            ans[i] = q+(49-s)
print(50)
print(*ans,sep = " ")