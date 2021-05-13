import sys
input = sys.stdin.readline

def main():
    N = int(input())
    xy = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: (x[0], x[1]))
    
    dic = {}
    max_ = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            p = xy[i][0] - xy[j][0]
            q = xy[i][1] - xy[j][1]
            if (p, q) in dic:
                dic[(p, q)] += 1
            else:
                dic[(p, q)] = 1
            max_ = max(max_, dic[(p, q)])
    
    print(N - max_)

if __name__ == "__main__":
    main()