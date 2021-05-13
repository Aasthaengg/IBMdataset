import sys
input = sys.stdin.readline

n,k= map(int, input().split())

if k>(n-1)*(n-2)//2:
    print(-1)

else:
    ans=[]
    # 1と他の点を繋ぐ
    for i in range(n-1):
        ans.append([1,i+2])

    v=(n-1)*(n-2)//2-k

    for i in range(2,n):
        for j in range(i+1,n+1):
            if v>0:
                ans.append([i,j])
                v-=1
            else:
                break

    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])