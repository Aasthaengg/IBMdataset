n,k = map(int,input().split())
a = list(map(int,input().split()))

tt = [0] * n
tt[0] = 1
ans_l = [1]
i = 1

for j in range(k):
    i = a[i-1]
    if tt[i-1] == False:
        tt[i-1] = 1
        ans_l.append(i)
    else:
        break

d = ans_l.index(i)
k -= d
ans = k % (len(ans_l)-d)
print(ans_l[ans+d])
