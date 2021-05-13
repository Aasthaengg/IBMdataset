import sys
input = sys.stdin.buffer.readline
import itertools

def main():
    N,K = map(int,input().split())
    if K > (N-1)*(N-2)//2:
        print(-1)
    else:
        ans = [(1,i+2) for i in range(N-1)]
        rest = (N-1)*(N-2)//2-K
        l = [i+2 for i in range(N-1)]
        c = 0
        for v in itertools.combinations(l,2):
            if c == rest:
                break
            else:
                ans.append(v)
                c += 1
        print(len(ans))
        for a,b in ans:
            print(a,b)

if __name__ == "__main__":
    main()