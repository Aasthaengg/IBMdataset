
# B Magic2
A, B, C = map(int, input().split())
K = int(input())
for i in range(K + 1):  # range()は0からなので+1
    for j in range(K + 1):
        for k in range(K + 1):
            if i + j + k <= K:  # K回以内
                if A * (2 ** i) < B * (2 ** j):
                    if B * (2 ** j) < C * (2 ** k):
                        print("Yes")
                        exit()
print("No")
