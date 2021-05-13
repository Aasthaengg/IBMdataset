#### ABC 085 C - Otoshidama
N, Y = map(int,input().split())

list_a = []
list_b = []
for a in range(N+1):
    for b in range(N+1):
        c = N - a - b
        if c >= 0:
            k = 10000 * a + 5000 * b + 1000 * c
            list_a.append(k)
            if Y == k:
                list_b.append(a)
                list_b.append(b)
                list_b.append(c)
        
if Y in list_a:
    print(str(list_b[0])+' '+str(list_b[1])+' ' + str(list_b[2])+' ')
if Y not in list_a:
    print('-1 ' + '-1 ' + '-1')