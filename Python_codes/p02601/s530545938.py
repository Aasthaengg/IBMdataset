def b_magic2():
    A, B, C = [int(i) for i in input().split()]
    K = int(input())

    count = 0
    while A >= B:
        count += 1
        B *= 2
    while B >= C:
        count += 1
        C *= 2
    return 'Yes' if count <= K else 'No'

print(b_magic2())