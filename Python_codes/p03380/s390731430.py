n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
mx = A[0]; A = A[1:]
mn = A[0]
for a in A[1:]:
    if abs(mn-mx/2) > abs(a-mx/2):
        mn = a
    else:
        break
print(mx, mn)