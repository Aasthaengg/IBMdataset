k = int(input())
l = list(map(int,input().split()))
for i in range(k-1,-1,-1):
    if i == k-1:
        if l[i] == 2:
            ans = [2,3]
        else:
            ans = [-1]
            break
    else:
        if l[i] > ans[1]:
            ans = [-1]
            break
        else:
            if l[i] >= ans[0]:
                ans[0] = l[i]
            else:
                b0 = ans[0]
                c = l[i]
                if b0%c == 0:
                    ans[0] = b0
                else:
                    if (b0//c+1)*c > ans[1]:
                        ans = [-1]
                        break
                    else:
                        ans[0] = (b0//c+1)*c
            b1 = ans[1]
            c = l[i]
            if b1%l[i] == 0:
                ans[1] = b1+l[i]-1
            else:
                ans[1] = (b1//c)*c+c-1
    
    #print(ans)
for i in ans:
    print(i,end=" ")