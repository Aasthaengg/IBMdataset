def b_magic2():
    A, B, C = [int(i) for i in input().split()]
    K = int(input())

    for j in range(K + 1):
        for k in range(K + 1):
            if j + k > K:
                break
            if A < B * (2**j) < C * (2**k):
                return 'Yes'
    return 'No'

print(b_magic2())