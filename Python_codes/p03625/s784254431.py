n = int(input())
a = list(map(int,input().split()))

dict1 = {}
for i in a:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

dict1_sorted = sorted(dict1.items(), key=lambda x:x[0], reverse = True)

ans = []

for a,b in dict1_sorted:
    if b >= 4:
        if len(ans) == 0:
            ans = [a] * 2
            break
        else:
            ans.append(a)
            break
    elif b >= 2:
        ans.append(a)
        if len(ans) == 2:
            break

if len(ans) == 2:
    print(ans[0] * ans[1])
else:
    print(0)
