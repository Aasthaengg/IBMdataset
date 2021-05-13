import sys
for i in sys.stdin.readlines(): 
    nums = list(map(int,i.split()))
    h = nums[0]
    w = nums[1]
    if h == 0 and w == 0:
        break
    for j in range(h):
        print("#"* w)
    print("")