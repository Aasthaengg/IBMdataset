# 500yen
A = int(input())
# 100
B = int(input())
# 50
C = int(input())
# total amount and 50 multiple of 50
X = int(input())

res = 0
for c500 in range(A+1):
    for c100 in range(B+1):
        for c50 in range(C+1):
            total = 500*c500 + 100*c100 + 50*c50
            if ( X == total):
                res += 1

print(res)