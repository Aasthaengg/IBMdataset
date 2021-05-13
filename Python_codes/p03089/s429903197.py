def main():
    from collections import deque
    N = int(input())
    B = deque(list(map(int, input().split())))
    result = deque([])
    for i in range(N):
        flag = False
        for j in range(len(B), 0, -1):
            b = B[j-1]
            if j == b:
                del B[j-1]
                result.append(b)
                flag = True
                break
        if not flag:
            print(-1)
            return
    for j in range(len(result)-1, -1, -1):
        print(result[j])
main()