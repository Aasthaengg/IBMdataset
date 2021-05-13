K = int(input())
S = input().split()
A = int(S[0])
B = int(S[1])

for i in range(A, B + 1):
    if i % K == 0:
        print("OK")
        exit()
print("NG")
