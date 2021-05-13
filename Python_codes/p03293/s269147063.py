S = str(input())
T = str(input())
n = len(S)
for i in range(n):
    S_ = S
    S_ = S_[i:]+S_[0:i]
    if S_ == T:
        print('Yes')
        break
else:
    print('No')