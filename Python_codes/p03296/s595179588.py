N = int(input())

def kansuu(list_x):
    result = []
    cnt = 1
    for i in range(len(list_x)-1):
        if list_x[i] == list_x[i+1]:
            cnt += 1
        else:
            num = list_x[i]
            result.append((num,cnt))
            cnt = 1
    result.append((list_x[-1],cnt))
    return result

a_li = list(map(int,input().split()))
ans = 0
for _,i in kansuu(a_li):
    if i == 1:
        continue
    else:
        ans += i//2
print(ans)
