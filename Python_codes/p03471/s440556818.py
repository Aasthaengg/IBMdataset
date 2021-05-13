nums = []
nums = input().split()
N = int(nums[0])
Y = int(nums[1])
Right = 0
for a in range(N+1) :
    for b in range(N + 1 - a):
        c = N - a - b
        if( Y == 10000 * a + 5000 * b + 1000 *c ):
            if (N == (a + b + c)):
                Right = 1
                break
            else:
                continue
    else:
        continue
    break
if( Right == 0 ):
    print("-1 -1 -1")
else :
    print(a,b,c)