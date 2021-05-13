n = int(input())
S = 100000
for i in range(n) :
    S *= 1.05
    if S % 1000!= 0 :
        S = (int(S/1000)+1)*1000
print(S)
