S = input()
temp = S[0]
K = 0
cnt = 1
for i in range(2, len(S)+1):
    if temp!=S[cnt:i]:
        temp = S[cnt:i]
        K+=1
        cnt = i
print(K+1)