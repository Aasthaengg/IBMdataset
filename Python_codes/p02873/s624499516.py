S = input()
a = [0]*(len(S)+1)

for i in range(len(S)):
    if S[i] is '<':
        a[i+1] = max(a[i+1], a[i]+1)
        

for i in range(1, len(S)+1):
    if S[-i] is '>':
        a[-(i+1)] = max(a[-(i+1)], a[-i]+1)
        
print(sum(a))