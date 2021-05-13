
"""
個数無制限ナップザック
大小判定は和が大きいほう→同じなら桁で比較していって先に大きくなった方
"""

N,M = map(int,input().split())

A = list(map(int,input().split()))

lis = [[0] * 10 for i in range(N+1)]
able = [False] * (N+1)
able[0] = True

nums = [0,2,5,5,4,5,6,3,7,6]

for i in A:

    for j in range(N):

        if able[j] and j+nums[i] <= N:

            if not able[j+nums[i]]:
                able[j+nums[i]] = True
                
                for k in range(10):
                    lis[j+nums[i]][k] = lis[j][k]

                lis[j+nums[i]][i] += 1

            else:

                flag = False

                if sum(lis[j+nums[i]]) < sum(lis[j]) + 1:
                    flag = True

                elif sum(lis[j+nums[i]]) == sum(lis[j]) + 1:

                    cp = lis[j].copy()
                    cp[i] += 1

                    for k in range(9,0,-1):

                        if lis[j+nums[i]][k] < cp[k]:
                            flag = True
                            break

                        elif lis[j+nums[i]][k] > cp[k]:
                            break


                if flag:
                    for k in range(10):
                        lis[j+nums[i]][k] = lis[j][k]
                    lis[j+nums[i]][i] += 1


ans = []

for i in range(9,0,-1):

    for j in range(lis[-1][i]):
        ans.append(i)

print ("".join(map(str,ans)))
