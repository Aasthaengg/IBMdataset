a, b, k = list(map(int, input().split()))
al, bl = [], []
if a == b:
    print(a)
else:   
    for i in range(min(b-a,k)):
        al.append(a+i)
        bl.append(b-i)
        ans = list(set(al) | set(bl))
    ans.sort()
    for i in ans:
        print(i)