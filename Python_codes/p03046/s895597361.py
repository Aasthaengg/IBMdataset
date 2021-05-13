M,K = (int(x) for x in input().split())

if M == 0:
    if K == 0:
        print("0 0")
        exit()
    else:
        print("-1")
        exit()
if M == 1:
    if K == 0:
        print("0 0 1 1")
        exit()
    else:
        print("-1")
        exit()

if K >= 2**M:
    print("-1")
    exit()

for i in range(2**M):
    if i != K:
        print(i, end=" ")
print(K, end=" ")
for i in range(2**M):
    if 2**M-1-i != K:
        print(2**M-1-i, end=" ")
print(K)

