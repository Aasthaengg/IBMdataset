def scc(W,F):
    a = W
    b = F
    c = a+b
    return c

W,F= input().split()
a = scc(F,W)
print(a)