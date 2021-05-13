N = int(input())
B = list(map(int,input().split()))
s = B[0]
for i in range(N-2):
    # print(i)
    if i == N - 2:
        s += B[i]
        # print(B[i])
        break
    else:
        if B[i] > B[i + 1]:
            s += B[i+1]
        else:
            s += B[i]
    # print(B[i])
s += B[N-2]
print(s)