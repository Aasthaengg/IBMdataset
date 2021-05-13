n , m = (int(a) for a in input().split())
ans = [0]*n
ng = [0]*n
NG = 0
for i in range(m) :
    p,s = input().split()
    p = int(p)
    if s == "AC" :
        if ans[p-1] == 0 :
            NG += ng[p-1]
            ans[p-1] = 1
    else :
        if ans[p-1] == 0 :
            ng[p-1] += 1
 
print(ans.count(1) , NG)