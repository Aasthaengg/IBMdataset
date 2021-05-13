N = int(input())
ls = list(map(int, input().split()))

def is_valid(a, b, c):
    valid = a != b and a != c and b != c
    is_triangle = a + b > c and b + c > a and c + a > b

    return valid and is_triangle


count = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if is_valid(ls[i], ls[j], ls[k]):
                # print(i+1, j+1, k+1)
                count += 1

print(count)
