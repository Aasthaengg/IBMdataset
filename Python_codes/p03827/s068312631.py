n = int(input())
S = input()
A = []
cur = 0
for i in S:
    if i == 'I':
        cur += 1
    else:
        cur -= 1
    A.append(cur)
    
print(max(max(A), 0))