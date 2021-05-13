N=int(input())
A=list(map(int,input().split()))

A_sum=0
a_start=0
for a in A:
    A_sum += abs(a_start-a)
    a_start=a
a=0
A_sum += abs(a_start-a)

A_=[0]
A_.extend(A)
A_.append(0)
for a_idx in range(1,len(A_)-1):
    a_before = A_[a_idx-1]
    a_ = A_[a_idx]
    a_after = A_[a_idx+1]
    print(A_sum-(abs(a_-a_before)+abs(a_-a_after)-abs(a_before-a_after)))