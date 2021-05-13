S = input()
K = int(input())
sl = []
for i in range(len(S)):
    for j in range(min(len(S) - i + 1,5)):
         sl.append(S[i:j+i+1])
sl = list(set(sl))
sl.sort()
print(sl[K-1])