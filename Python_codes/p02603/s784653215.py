def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.append(0)
    pre = 10**9
    kabu = 0
    ans = 1000
    flag1,flag2 = False,False
    if a[0]<a[1]:
        flag2 = True
    else:
        flag1 = True
    for i in range(n+1):
        if flag1==True and a[i]> pre:
            kabu += ans//pre
            ans -= kabu*pre
            flag1,flag2 = False,True
        elif flag2==True and a[i]<pre:
            ans += kabu*pre
            kabu = 0
            flag1,flag2 = True,False
        pre = a[i]
        #print(ans,kabu)
    print(ans)

main()