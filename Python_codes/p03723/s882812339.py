li = list(map(int,input().split()))
nx = [0,0,0]
ans = 0
if all(x&1 == 0 for x in li) and li[0] == li[1] == li[2]:
    print(-1)
else:
    while 1:
        if(li[0]%2!=0 or li[1]%2!=0 or li[2]%2!=0):
            break
        nx[0] = (li[1] + li[2])/2
        nx[1] = (li[0] + li[2])/2
        nx[2] = (li[0] + li[1])/2
        li = nx.copy()
        ans += 1
    print(ans)



    

