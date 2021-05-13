X,K,D = list(map(int,input().split()))
max_number = X + K*D
min_number = X - K*D
if min_number >= 0:
    ans = min_number
elif max_number <= 0:
    ans = -max_number
else:
    q = max_number // (2*D)
    ans1 = max_number - 2*q*D
    ans2 = max_number - 2*(q+1)*D
    if ans1 > -ans2:
        ans = -ans2
    else:
        ans = ans1
print(ans)
