n,c= map(int,input().split())
nca = sorted([tuple(map(int,input().split())) for _ in range(n)])
cnf = [True]*n
line=0
while any(cnf):
    lst = ()
    for i in range(n):
        if cnf[i]==True:
            temp = nca[i]
            if (lst == ()) or (temp[2]==lst[2]) or (lst[1] < temp[0]):
                lst = temp
                cnf[i]=False
    line+=1
print(line)