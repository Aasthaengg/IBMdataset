n = int(raw_input())

nums = [[[0 for x in range(10)] for x in range(3)] for x in range(4)]

for idx in range(n):

    b, f, r, v  = tuple([int(x) for x in raw_input().split(" ")])
    nums[b-1][f-1][r-1] += v

for i_b in range(4):
    if i_b != 0: print "#"*20
    for i_f in range(3):
        print " " + " ".join([str(x) for x in nums[i_b][i_f]])