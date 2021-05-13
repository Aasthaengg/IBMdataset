N = int(input())
A = list(map(int,input().split()))
dic = {}
for i in range(N):
    data = A[i]
    if data in dic:  dic[data] += 1
    else:  dic[data] = 1
temp1, temp2 = 0, 0
for i in sorted(dic.keys())[::-1]:
    if dic[i] >= 2:
        if temp1 == 0:  
            temp1 = i
            if dic[i] >= 4:
                temp2 = i
                break
        else:
            temp2 = i
            break
ans = temp1 * temp2
print(ans)