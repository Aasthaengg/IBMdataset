n = int(input())
s = input()

num = '0123456789'
cnt = 0
for i in num:
    for j in num:
        for k in num:
            if i in s:
                idx1 = s.find(i)
                if j in s[idx1 +1 :]:
                    idx2 = s.find(j, idx1 + 1)
                    if k in s[idx2 + 1:]:
                        idx3 = s.find(k, idx2 + 1)
                        cnt += 1
print(cnt)