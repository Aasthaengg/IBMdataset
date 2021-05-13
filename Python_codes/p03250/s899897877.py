a = list(map(int,input().split()))
a.sort()

A = a[2]
B = a[1]
C = a[0]


ans = max(A+int(str(B) + str(C)),int(str(A) + str(B))+C)
print(ans)