#リストAの丸太を全てx以下にK回以内の切る回数で揃えることができるかを判断する関数。
def can_or_cannot(A,K,x):
    kaisuu_sum = 0
    for i in range(len(A)):
        if A[i]%x == 0:
            temp = (A[i]//x) - 1
            kaisuu_sum += temp
        else:
            temp = A[i]//x
            kaisuu_sum += temp

        if kaisuu_sum > K:
            return 'No'

    return 'Yes'

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #二分探索するよ
    left = 0
    right = A[N-1]

    if right == 1:
        return 1

    mid = 0
    while True:
        if right == 1:
            return 1
            
        mid = int( (left + right)/2 )
        #print(left,mid,right)
        judge = can_or_cannot(A,K,mid)
        #print(left,mid,right,judge)
        if judge == 'No':
            left = mid+1
        elif judge == 'Yes':
            right = mid

        if left == right:
            #print(left,mid,right)
            return right

print(main())
