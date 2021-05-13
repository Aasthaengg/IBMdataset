from collections import defaultdict

def main():
    N = int(input())
    robots = []
    for _ in range(N):
        x,l = [int(x) for x in input().split()]
        robots.append((x-l, x+l))

    # print(sorted(robots.items(), key=lambda x:x[1]))
    cnt = 0
    t = -float('inf')
    for start,end in sorted(robots, key=lambda x:x[1]):
        # print(t,start)
        if t <= start:
            # print('append')
            cnt += 1
            t = end
    print(cnt)
        

if __name__ == '__main__':
    main()