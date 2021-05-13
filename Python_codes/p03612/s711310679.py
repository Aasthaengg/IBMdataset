n = int(input())
p_li = list(map(int,input().split()))
dum = 0
ans = 0
flag = 0
count = 0
for i in range(n):
    if i+1 == p_li[i]:
        ans += 1
        if flag == 1:
            if dum == i-1:
                count += 1
                flag = 0
        else:
            flag = 1
        dum = i

#div,mod = divmod(dum,2)
print(ans-count)
