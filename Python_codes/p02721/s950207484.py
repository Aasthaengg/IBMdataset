a,b,c = map(int,(input().split()))
mb = input()
 
rl = list()
ll = list()
 
for i in range(a):
    if mb[i] == "x":continue
    if len(rl) == 0:
        rl.append(i + 1)
    else:
        if rl[-1] + c + 1 <= i + 1:
            rl.append(i + 1)
            if len(rl) == b:break
 
for i in range(a-1,-1,-1):
    if mb[i] == "x":continue
    if len(ll) == 0:
        ll.append(i + 1)
    else:
        d1 = ll[-1] - c - 1
        d2 = i + 1
        if  d1 >= d2:
            ll.append(i + 1)
            if len(ll) == b:break
 
ans=list()
for i,k in zip(rl,reversed(ll)):
    if b == 1 and len(rl) != 1 or b==0:break
    if i == k:
        ans.append(i)
 
[print(i) for i in ans]