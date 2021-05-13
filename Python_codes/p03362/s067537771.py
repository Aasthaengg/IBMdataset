def sosuu(A, cnt):
    sosuu=[2]
    ans=[] # 5n+1の素数
    for L in range(3,A,2):
        for L2 in sosuu:
            if L%L2==0:
                break
        else:
            sosuu.append(L)
            if L%5==1:
                ans.append(L)
                cnt-=1
                if cnt==0:
                    break
    return ans
n=int(input())
print(*sosuu(55555,n))
