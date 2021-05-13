N = int(input())
C = [int(input()) for _ in range(N)]
C = [x for x,y in zip(C[:-1],C[1:]) if x!=y] + [C[-1]]

DP = [1]
dic = {}

for i in range(len(C)):   
    DP.append((DP[-1]+dic.get(C[i],0))%(10**9+7))    
    dic[C[i]] = DP[-1]
print(DP[-1])          