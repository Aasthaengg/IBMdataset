n,x=list(map(int, input().split()))
l=list(map(int, input().split()))
res = 1
hane = 0
for i in range(n):
    hane += l[i]
    if hane <= x: res +=1
    else : break
print(res)
