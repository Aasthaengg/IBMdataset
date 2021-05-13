import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    order_F = []
    order_F = input().rstrip().split('T')
    x, y = map(int, input().split())
    vert_DP = [False] * 8001
    side_DP = [False] * 8001
    vert_DP[0] = True
    side_DP[0] = True
    vert_sum = 0
    side_sum = 0
    distance = [len(order_F[i]) for i in range(len(order_F))]
    order_len = len(order_F)
    x -= len(order_F[0])
    vert_last = 0
    side_last = 0
    for i in range(1, order_len):
        if i % 2 == 0:
            side_sum += distance[i]
            for j in reversed(range(side_last+1)):
                if side_DP[j]:
                    side_DP[j + distance[i]] = True
            side_last += distance[i]
        else:
            vert_sum += distance[i]
            for j in reversed(range(vert_last+1)):
                if vert_DP[j]:
                    vert_DP[j + distance[i]] = True
            vert_last += distance[i]
    if side_sum < x or vert_sum < y:
        print("No")
    elif (side_sum - x) % 2 == 1 or (vert_sum - y) % 2 == 1:
        print("No")
    else:
        if side_DP[(side_sum - x)//2] and vert_DP[(vert_sum - y)//2]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
