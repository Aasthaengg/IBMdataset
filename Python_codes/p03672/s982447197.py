S = list(input())
num = len(S)
for i in range(num):
    S.pop()
    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        break
    
