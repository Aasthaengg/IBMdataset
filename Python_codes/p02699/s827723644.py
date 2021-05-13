
R = input()
S = R.split(' ')[0]
W = R.split(' ')[1]

if int(S) <= int(W) :
    print("unsafe")
else :
    print("safe")