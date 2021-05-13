a = list(input())
b = list(input())
c = len(a)
d = len(b)
if d > c:
    print("UNRESTORABLE")
    exit()
ans = []
   
for i in range(c-d+1):
    #print(a[i:i+d])
    flag = False
    for j in range(d):
        if a[i:i+d][j] == b[j] or a[i:i+d][j] == "?":
            flag = True
        else:
            flag = False
            break
    li = [] 
    if flag:
        #print(a[i:i+d])
        li = a[:i] + b + a[i+d:]
        for k in range(len(li)):
            if li[k] == "?":
                li[k] = "a"
        ans.append("".join(li))
if ans:
    ans.sort()
    print(ans[0])
else:
    print("UNRESTORABLE")