n = int(input())
B = list(map(int, input().split()))
C = []
C.append(B[0])
for i in range(len(B) - 1):
    C.append(min(B[i], B[i+1]))
C.append(B[-1])
print(sum(C))



