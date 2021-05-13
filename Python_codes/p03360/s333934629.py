def resolve():
    a = list(map(int, input().split()))
    K = int(input())
    print(sum(a)-max(a)+max(a)*(2**K))
resolve()