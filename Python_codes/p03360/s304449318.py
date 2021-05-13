def actual(a, b, c, k):
    # 2倍されるのは 1つの数字に限られるので、そいつだけを2倍していけばいい
    max_num = max((a, b, c))
    repetition = (2 ** k - 1)
    
    return a + b + c + (max_num * repetition)

a, b, c = map(int, input().split())
k = int(input())

print(actual(a, b, c, k))
