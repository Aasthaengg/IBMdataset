n = int(input())
A = list(map(int,input().split()))
s1 = s2 =  0
#偶数番目までの和を正→ans1、奇数番目までの和を正→ans2
ans1 = ans2 = 0
#ans1について
for i in range(len(A)):
    s1 += A[i]
    if (i+1)%2==0:
        if s1>0:
            continue
        else:
            ans1+= abs(s1) + 1
            s1 = 1
    else:
        if s1<0:
            continue
        else:
            ans1 += abs(s1) +1
            s1 = -1
#ans2について
for i in range(len(A)):
    s2 += A[i]
    if (i+1)%2 == 0:
        if s2 <0:
            continue
        else:
            ans2 += abs(s2) + 1
            s2 = -1
    else:
        if s2 > 0:
            continue
        else:
            ans2 += abs(s2) + 1
            s2 = 1
print(min(ans1,ans2))