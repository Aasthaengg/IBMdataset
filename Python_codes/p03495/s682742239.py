def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    balls = {}
    bucket = [[] for _ in range(n+1)]

    for ball in A:
        if ball in balls:
            balls[ball] += 1
        else:
            balls[ball] = 1
    
    for key, value in balls.items():
        bucket[value].append(key)

    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            if bucket[i] != [] and len(balls) > k:
                res += i
                balls.pop(bucket[i][j])

    print(res)

if __name__ == '__main__':
    main()