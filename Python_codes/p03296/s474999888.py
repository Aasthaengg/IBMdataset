def run_length(a):
    result = []
    N = len(a)
    cnt = 1
    for i in range(N):
        if i == N - 1 or a[i] != a[i + 1]:
            result.append(cnt)
            cnt = 1
        else:
            cnt += 1
    return result

N = int(input())
a = list(map(int, input().split()))

print(sum(map(lambda x: x // 2, run_length(a))))