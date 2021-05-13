n=int(input())
an=list(map(int, input().split()))

def check(sign):
    a_cnt=0
    a_sum=0
    for a in an:
        a_sum+=a
        if a_sum*sign<=0:
            a_cnt+=abs(a_sum-sign)
            a_sum=sign
        sign*=-1

        # print(a_sum, a_cnt)

    return a_cnt

print(min(check(1),check(-1)))
