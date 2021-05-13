N = int(input())
A = [int(i) for i in input().split(" ") ]
odd = [2 if i%2==0 else 1 for i in A]

# 条件1|x_i-y_i|<=1を満たすパターン数を出す
PI1 = 3**N
# 条件2の対偶(総積が奇数ならカウントしない)のパターンを条件1のパターンから引く
PI2 = 1
for i in odd:
    PI2*=i
    
print(PI1-PI2)
