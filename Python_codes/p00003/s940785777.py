def triangle(dataset):
    a, b, c = dataset
    if a*a + b*b == c*c:
        return 1
    return 0

N = int(input())
for _ in range(N):
    dataset = sorted(map(int, input().split()))
    flag = triangle(dataset)
    print(["NO", "YES"][flag])