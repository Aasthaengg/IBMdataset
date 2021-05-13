N=int(input())
A=list(map(int,input().split()))
heikin=sum(A)/N
kouho = []

if heikin in A:
    print(A.index(heikin))
else:
    for i in A:
        kouho.append(abs(heikin-i))
    ans = kouho.copy()
    ans.sort()
    print(kouho.index(ans[0]))