alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
DP = [[] for i in range(10)]
DP[0] = ['a']
for i in range(9):
    for w in DP[i]:
        num = alpha.index(w[0])
        for i in range(1,len(w)):
            num = max(num, alpha.index(w[i]))
        for j in range(num+1):
            DP[i+1].append(w + alpha[j])
        if num + 1 <= 9:
            DP[i+1].append(w + alpha[num+1])
N  = int(input())
for w in DP[N-1]:
    print(w)