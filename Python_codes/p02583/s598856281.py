n = int(input())
L = list(map(int,input().split()))
print(sum([1 if not(L[i]==L[j] or L[i]==L[k] or L[j]==L[k]) and L[i]+L[j] > L[k] and L[i]+L[k] > L[j] and L[j]+L[k] > L[i] else 0 for i in range(0,n) for j in range(i+1,n) for k in range(j+1,n)])) 