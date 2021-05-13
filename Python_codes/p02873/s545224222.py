S = input()
a = [0 for i in range(len(S)+1)]
for i, x in enumerate(S):
    if x == '<':
        a[i+1] = max(a[i+1], a[i]+1)
for i in range(len(S)):
    if S[-i-1] == '>':
        a[-i-2] = max(a[-i-2], a[-i-1]+1)
print(sum(a)) 
