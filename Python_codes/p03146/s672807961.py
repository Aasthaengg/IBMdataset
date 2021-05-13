s = int(input())
ans = [0]*1000001
for i in range(1,1000001):
    if i == 1:
        a = s
        ans[a] +=1
    else:
        if a%2 == 0:
            a = a//2
            ans[a] += 1
        else:
            a = 3*a+1
            ans[a] +=1
        if ans[a] ==2:
            print(i)
            break
