N = int(input())
S = input()
r = S.count("R")
g = S.count("G")
b = S.count("B")
ans = r*g*b
for i in range(0,N-2) :
    for j in range(i+1,N-1) :
        k = j + (j - i)
        if k < N :
            if (S[i] != S[j]) and (S[i] != S[k]) and (S[j] != S[k]) :
                ans -= 1
print(ans) 