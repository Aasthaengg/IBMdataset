n,k = (int(a) for a in input().split())
r,s,p = (int(a) for a in input().split())
T = list(input())
point = 0
for i in range(n) :
    if i < k :
        pass
    elif  T[i] == T[i-k] :
        T[i] = 0
a = T.count("r")
b = T.count("s")
c = T.count("p")
print(a*p + r*b + c*s)


