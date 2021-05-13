A, B = map(int, input().split())
print(100,100)

L = [['#' for _ in range(100)] for _ in range(50) ]+ [['.' for _ in range(100)] for _ in range(50)]
i = 0
k = 0
for _ in range(A-1):
    try :
        L[i][k] = '.'
        k += 2
    except:
        i += 2
        k = 0
        L[i][k] = '.'
        k += 2
L = L[::-1]
i = 0
k = 0
for _ in range(B-1):
    try :
        L[i][k] = '#'
        k += 2
    except:
        i += 2
        k = 0
        L[i][k] = '#'
        k += 2
for x in L:
    for y in x:
        print(y,end ='')
    print()
