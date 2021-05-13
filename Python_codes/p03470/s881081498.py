def actual(N, D):
    # バケット法
    bucket = dict()

    for num in D:
        if num in bucket.keys():
            bucket[num] += 1
        else:
            bucket[num] = 1

    return len(bucket)

N = int(input())
D = [int(input()) for _ in range(N)]

print(actual(N, D))