import sys

def solve(A,B,K):
    ab = [A,B]
    for i in range(K):
        if ab[0]%2!=0:
            ab[0]-=1
        ab[1]+=ab[0]//2
        ab[0]-=ab[0]//2
        ab.reverse()
    if K%2!=0:
        print(ab[1],ab[0])
        return
    print(ab[0],ab[1])


def readQuestion():
    ws = sys.stdin.readline().strip().split()
    A = int(ws[0])
    B = int(ws[1])
    C = int(ws[2])
    return (A, B, C)

def main():
    solve(*readQuestion())
    

# Uncomment before submission
main()