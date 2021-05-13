from sys import stdin

while True:
    H, W = [int(x) for x in stdin.readline().rstrip().split()]
    if H == 0 and W == 0:
        break
    else:
        print("#"*W)
        for i in range(H-2):
            print("#"+"."*(W-2)+"#")
        else:
            print("#"*W + "\n")

