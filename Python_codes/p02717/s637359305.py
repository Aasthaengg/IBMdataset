# 160 A

def swap(l, a, b, c):
    l[a], l[b] = l[b], l[a] 
    l[a], l[c] = l[c], l[a]
    return l

k = list(map(int, input().split()))
swap(k, 0, 1, 2)
for i in k:
    print(i, end  = " ")