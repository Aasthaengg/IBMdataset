K = int(input())
A = [int(i) for i in input().split()][::-1]

cb, cu = 2, 2
for a in A:
    nb = ((cb+a-1)//a)*a
    nu = (cu//a+1)*a-1
    if nb > cu:
        print(-1)
        exit()
    cb, cu = nb, nu
print(nb, nu)
