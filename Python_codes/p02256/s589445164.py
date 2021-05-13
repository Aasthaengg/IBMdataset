targ = [int(n) for n in input().split(' ')]
big,small = max(targ),min(targ)
while big % small != 0:
    disp = small
    small = big % small
    big = disp
print(small)