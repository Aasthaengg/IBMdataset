def resolve():
    n, m = map(int, input().split())
    ans = list()

    for i in range(n):
        ans.append(0)    

    for i in range(m):
        a, b = map(int, input().split())
        ans[a-1] +=1
        ans[b-1] +=1
    
    for i in range(n):
        print(ans[i])
resolve()