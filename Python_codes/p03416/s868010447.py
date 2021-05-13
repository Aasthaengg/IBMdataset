A,B = map(str,input().split())
cnt = 0
for i in range(int(A),int(B)+1):
    l = list(str(i))
    flag = True
    n = len(l)
    for j in range(n//2):
        if l[j] != l[n-j-1]:
            flag = False
    
    if flag:
        cnt += 1

print(cnt)
