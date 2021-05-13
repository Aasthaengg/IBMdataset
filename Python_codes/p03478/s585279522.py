N,A,B= input().split()
l = [N,A,B]
N,A,B = map(int,l)

m = 0

for i in range(1,N+1):

    n = 0
    
    for j in range(len(str(i))):

        n += int(str(i)[j])

    if A <= n <= B:
        m += i

print(m)

