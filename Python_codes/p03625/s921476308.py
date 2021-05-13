N = int(input())
A = list(map(int,input().split()))

from collections import Counter

A_=Counter(A)
A_.most_common()

Rectangle = [_ for _ in A_.keys() if A_[_] >1]
sq_list=[_ for _ in A_.keys() if A_[_] >= 4]

Rectangle.sort()
sq_list.sort()

ans=0

if len(Rectangle) >= 2:
    a_1 = Rectangle[-1]
    a_2 = Rectangle[-2]
    ans = a_1*a_2
    
if len(sq_list) >= 1:
    s_1 = sq_list[-1]
    if ans < s_1**2:
        ans=s_1**2

print(ans)