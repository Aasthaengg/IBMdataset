if __name__ == '__main__':
    n, k = map(int, input().split())
    total = 0
    data = []
    
    for i in range(n):
        data.append(int(input()))
        total += data[i]

    def check(weight):
        i = 0
        for j in range(k):
            s = 0
            while s + data[i] <= weight:
                s += data[i]
                i += 1
                if i == n:
                    return n
        return i

    def solve():
        left = 0
        right = total + 1
        
        while right > left:
            mid = (right + left)//2
            c = check(mid) # 检查当每辆车的装载量为 mid 时，最多能装多少件货物
            if c >= n:
                right = mid
            else:
                left = mid + 1
        return right

    print(solve())

