N = int(input())
K = 'Christmas'
if N < 25:
    for i in range(25-N):
        K = K + ' Eve'
print(K)