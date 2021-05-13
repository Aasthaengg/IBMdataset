a,b,c,k = map(int, input().split())
cheak = 10**18
ans = a-b
def calc(a,b,c,k):
    if a == b:
        return 0
    elif ans < 0:
        if k % 2 == 1:
            return -ans
        else:
            return ans
    else:
        if k % 2 == 1:
            return -ans
        else:
            return ans
ans_n = calc(a,b,c,k)
if ans_n > cheak:
    print("Unfair")
else:
    print(ans_n)
