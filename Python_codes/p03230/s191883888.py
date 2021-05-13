N = int(input())

def gen_set(k):
    s = [[0] * k for _ in range(k + 1)]

    for i in range(k + 1):
        if i == 0:
            s[i][0] = 1
            for j in range(1, k):
                s[i][j] = s[i][j - 1] + j    
        elif 1 <= i < k:
            s[i][0] = s[0][i]
            for j in range(1, k):
                if j <= i:
                    # Horizontal
                    s[i][j] = s[i][j - 1] + 1
                else:
                    # Vertical
                    s[i][j] = s[i][j - 1] + j
        else:
            # Diagonal
            s[i][0] = s[0][0]
            for j in range(1, k):
                s[i][j] = s[i][j - 1] + j + 1

    return s


x = 0
k = 0
while x < N:
    k += 1
    x += k

if x == N:
    s = gen_set(k)
    print("Yes")
    print(k + 1)
    for t in s:
        print(k, *t)
else:
    print("No")
