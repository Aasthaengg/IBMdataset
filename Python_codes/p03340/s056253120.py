def shakutori(a):
    left =0
    right = 0
    su = 0
    su1 = 0
    ans = 0
    for left in range(len(a)):
        while right<len(a) and su+a[right]==su1^a[right]:
            su +=a[right]
            su1 = su1^a[right]
            right +=1
        ans+=right -left
        if left==right:
            right+=1
        else:
            su -=a[left]
            su1 ^= a[left]
    return ans
N = int(input())
A = [int(x) for x in input().split()]
print(shakutori(A))