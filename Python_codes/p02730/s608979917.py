S = list(input())
k = (len(S) -1) // 2 
T = S[0:k]
#print(T[::-1])
print("Yes" if S == S[::-1] and T == T[::-1] else "No")