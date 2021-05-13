H = int(input())
W = int(input())
N = int(input())
def paint(H,W,N):
    large = max(H,W)
    if N/large == int(N/large):
        return int(N/large)
    else:
        return int (N/large)+1
print(paint(H,W,N))