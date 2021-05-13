import sys

for line in sys.stdin:
    [H,W] = [int(x) for x in line.split()]
    if [H,W] == [0,0]:
        break
    print( ("#" * W +"\n") * H)