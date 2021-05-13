from collections import deque
dq = deque([1,2,3,4,5,6,7,8,9])
ans = []
while dq:
    p = dq.popleft()
    ans.append(p)
    if p <= 323456666:
        q = p % 10
        if not q in [0,9]:
            for i in range(-1,2):
                dq.append(10*p+q+i)
        else:
            if q == 9:
                dq.append(10*p+8)
                dq.append(10*p+9)
            else:
                dq.append(10*p)
                dq.append(10*p+1)
ans.sort()
#print(ans)
print(ans[int(input())-1])