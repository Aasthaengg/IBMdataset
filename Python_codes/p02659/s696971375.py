A,B = input().split()
A = int(A)
ans = 0
cnt = 0
for s in B:
    if(s=='.'):
        continue
    else:
        s = int(s)
        ans += A * (10**(2-cnt)) * s
        cnt += 1

ans = ans//100
#print(type(ans))
print(ans)