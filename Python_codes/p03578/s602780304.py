n=int(input())
d=sorted(map(int,input().split()))
m=int(input())
t=sorted(map(int,input().split()))

d_dic = dict()
t_dic = dict()

for i in range(n):
    d1 = d[i]
    if d1 not in d_dic.keys():
        d_dic[d1] = 1
    else:
        d_dic[d1] += 1

ans = 0

for i in range(m):
    t1 = t[i]
    if t1 in d_dic.keys():
        d_dic[t1] -= 1
        if d_dic[t1] < 0:
            ans = 1
            break
    else:
        ans = 1
        break
    
if ans == 1:
    print("NO")
else:
    print("YES")