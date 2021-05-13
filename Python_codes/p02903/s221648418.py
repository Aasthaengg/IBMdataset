from itertools import chain

def solve(H,W,A,B):

    return '\n'.join(chain(('1'*A+'0'*(W-A) for _ in range(B)), ('0'*A+'1'*(W-A) for _ in range(H-B))))




if __name__ == '__main__':
    H,W,A,B = map(int,input().split())
    print(solve(H,W,A,B))