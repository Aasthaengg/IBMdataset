N = int(input())
A = list(map(int, input().split()))

B = [a-1 for a in A]
C = [a+1 for a in A]


def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

count = 0
for i in range(3**N):
    i3 = Base_10_to_n(i, 3).zfill(N)
    Pick = []
    for j in range(N):
        if i3[j] == '0':
            Pick.append(A[j])
        elif i3[j] == '1':
            Pick.append(B[j])
        elif i3[j] == '2':
            Pick.append(C[j])
#    print(i3, ':', Pick)
    if any([p%2 == 0 for p in Pick]):
        count += 1
print(count)