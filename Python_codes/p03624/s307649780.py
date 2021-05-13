#B - Not Found
S = list(input())
S = sorted(S)
S = set(S)

A = [chr(o) for o in range(ord('a'),ord('z')+1)]
result = 'None'
for i in A:
    if i in S:
        continue
    else:
        result = i
        break
print(result)