while True:
    n=str(input())
    if n=='-':
        break
    N=len(n)
    n_list=list(n)
    m=int(input())
    for i in range(m):
        h=int(input())
        for j in range(h):
            A=n_list[0]
            n_list.remove(n_list[0])
            n_list.append(A)
    C=''.join(n_list)
    print(C)
