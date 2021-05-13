n,a,b = map(int,input().split())
n_list = [0 for i in range(n)]
n_list[a-1] = 1
n_list[b-1] = 2
i = 0
a = a-1
b = b-1
alice = True
borys = True
while True:
    if n_list[a+1] == 0:
        n_list[a] = 0
        n_list[a+1] = 1
        a += 1
    else:
        if a-1 >= 0:
            n_list[a] = 0
            n_list[a-1] = 1
            a -= 1
        else:
            alice = False
            break
    if n_list[b-1] == 0:
        n_list[b] = 0
        n_list[b-1] = 2
        b -= 1
    else:
        if b+1 <= n-1:
            n_list[b] = 0
            n_list[b+1] = 2
            b += 1
        else:
            borys = False
            break
    if alice == False or borys == False:
        break
if alice == False:
    print('Borys')
else:
    print('Alice')
