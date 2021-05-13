n,c = map(int,input().split())
xv = [list(map(int, input().split())) for i in range(n)]

# 右まわり
right = [[0,0]]
for i in range(n):
    right.append([xv[i][0],right[-1][1]+xv[i][1]])

right_best =[0]
for i in range(1,len(right)):
    right_best.append(max(right[i][1]-right[i][0],right_best[-1]))

right_return_best = [0]
for i in range(1,len(right)):
    right_return_best.append(max(right[i][1]-right[i][0]*2,right_return_best[-1]))


# 左回り
for i in range(n):
    xv[i][0]=c-xv[i][0]
xv.reverse()

left = [[0,0]]
for i in range(n):
    left.append([xv[i][0],left[-1][1]+xv[i][1]])

left_best =[0]
for i in range(1,len(left)):
    left_best.append(max(left[i][1]-left[i][0],left_best[-1]))

left_return_best = [0]
for i in range(1,len(left)):
    left_return_best.append(max(left[i][1]-left[i][0]*2,left_return_best[-1]))


# 答え計算
ans = 0
for i in range(n+1):
    ans = max(ans,left_best[i]+right_return_best[n-i], right_best[i]+left_return_best[n-i])

print(ans)