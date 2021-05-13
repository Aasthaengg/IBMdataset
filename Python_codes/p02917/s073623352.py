N = int(input())
B = list(map(int,input().split()))

# 双対考える
# A1<=B1, A2<= min(B1,B2), A3<=min(B2,B3) ...
A = [B[0]]

for i in range(N-1):
    if i+1 != len(B):
        A.extend([min(B[i],B[i+1])])
    else:
        A.extend([B[i]])


print(sum(A))