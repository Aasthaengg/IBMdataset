A,B,C,D = map(int,list(input()))

dic = { 1:"+" , -1:"-"}

import itertools
for AB,BC,CD in itertools.product([1,-1],repeat=3):
    tmp = A + B*AB + C*BC + D*CD

    if tmp ==7:
        ans = str(A)+dic[AB]+str(B)+dic[BC]+str(C)+dic[CD]+str(D)+"=7"
        print(ans)
        exit()