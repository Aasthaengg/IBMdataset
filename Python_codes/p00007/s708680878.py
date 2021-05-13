n=int(input())
S=100000
for i in range(n):
    S = S*1.05
    R = S%1000
    if R:
        S = S-R+1000
print(int(S))
