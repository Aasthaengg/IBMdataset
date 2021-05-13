def search(a, s):
    min_i = 0
    max_i = len(a)-1
    i = int(len(a)/2)

    if a[min_i] < s and s < a[max_i]:
        while True:
            if a[i] <= s and s < a[i+1]:
                break
            elif s < a[i]:
                max_i = i
                i = min_i + int((max_i - min_i)/2)
            else:
                min_i = i
                i = min_i + int((max_i - min_i)/2)

        return i
    elif s <= a[min_i]:
        return min_i
    else:
        return max_i

N,M,K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_SUM = [0]
B_SUM = [0]

for i in range(N):
    A_SUM.append(A[i] + A_SUM[i])

for j in range(M):
    B_SUM.append(B[j] + B_SUM[j])

count = 0
for i in range(N+1):
    if K >= A_SUM[i]:
        a = K - A_SUM[i]
        j = search(B_SUM, a)
        if count < i + j:
            count = i + j

print(count)
