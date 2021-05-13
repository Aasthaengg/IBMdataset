N = int(input())
A = list(map(int,input().split()))

l,r = 0,0
num = 0
ans = 0
while r<N:
    if num^A[r] == num + A[r]:
        num += A[r]
        r += 1
        ans += r-l
        #print(l,r,num)
    else:
        if l==r:
            l += 1
            r += 1
            #print(l,r,num)
        else:
            num -= A[l]
            l += 1
            #print(l,r,num)
print(ans)