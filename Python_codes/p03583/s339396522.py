N = int(input())
s = 1
for i in range(1,3501):
    if s == 0:
        break
    for j in range(1,3501):
        if 4*i*j-N*(i+j) > 0 and (N*i*j)%(4*i*j-N*(i+j)) == 0:
            print(i,j,(N*i*j)//(4*i*j-N*(i+j)))
            s = 0
            break