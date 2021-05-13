# a_i <= b_iなら同じidxを選ぶことで揃えられる

# 操作A : a_i > b_i で b_i +=1
# sum(a-b)回「行う必要がある」

# 操作B : a_j < b_j で (この条件を外れない範囲まで)a_j +=2
# sum((b-a)//2) 回「まで行える」
# ex. b-a==1 なら操作Bは行えない

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

la = 0
lb = 0
for i in range(N):
    if a[i] > b[i]:
        la += a[i] - b[i]
    elif b[i] > a[i]:
        lb += (b[i] - a[i]) // 2

if lb >= la:
    print("Yes")
else:
    print("No")
