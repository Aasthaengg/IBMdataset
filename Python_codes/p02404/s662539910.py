import sys
for i in sys.stdin.readlines(): 
    nums = list(map(int,i.split()))
    h = nums[0]
    w = nums[1]
    if h == 0 and w == 0:
        break
    for j in range(1,h+1):
        if j == 1 or j == h:
            print("#"* w)
        else:
            print("#" + "."*(w-2) + "#")
    print("")