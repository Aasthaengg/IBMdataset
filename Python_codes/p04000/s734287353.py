def solve():
    diff = [(i-1,j-1) for i in range(3) for j in range(3)]
    H,W,N = map(int, input().split())
    count_dict = {}
    ret = [0]*10
    ret[0] = (W-2)*(H-2)
    for i in range(N):
        a, b = map(int,input().split())
        # da = min(a, W-a, 2)+1
        # db = min(b, H-b, 2)+1
        # rect_num = da*db
        for da,db in diff:
            ra, rb = a+da, b+db
            if ra <= 1 or ra >= H or rb <= 1 or rb >= W : continue
            # if (ra,rb) == (4,2): print(i+1, a, b, ra, rb)
            if (ra,rb) in count_dict:
                dom = count_dict[(ra,rb)]
                ret[dom] -= 1
                ret[dom+1] += 1
                count_dict[(ra,rb)] += 1
            else:
                ret[0] -= 1
                ret[1] += 1
                count_dict[(ra,rb)] = 1
                
    # print(count_dict)
    print('\n'.join(map(str,ret)))
    
solve()