a,b = map(int,input().split())

w_o = [['.' for i in range(3)] for j in range(3)]
b_o = [['#' for i in range(3)] for j in range(3)]

        
w_c = [['#' for i in range(3)] for j in range(3)]
b_c = [['.' for i in range(3)] for j in range(3)]

w_c[1][1] = '.'
b_c[1][1] = '#'

ab = [['.' for i in range(99)] for j in range(99)]

a -= 1
b -= 1

a_y = a//33
a_x = a % 33

for i in range(17):
    for j in range(33):
        if a_y > i:
            #w_c
            for k in range(3):
                for l in range(3):
                    ab[i*3+k][j*3+l] = w_c[k][l]
        elif a_y == i:
            if a_x > j:
                for k in range(3):
                    for l in range(3):
                        ab[i*3+k][j*3+l] = w_c[k][l]
            else:
                for k in range(3):
                    for l in range(3):
                        ab[i*3+k][j*3+l] = w_o[k][l]
        else:
            for k in range(3):
                for l in range(3):
                    ab[i*3+k][j*3+l] = w_o[k][l]

if a > 0:
    b -= 1

if b == -1:
    print(51,99)
    for i in range(51):
        print(*ab[i],sep="")
    exit()

b_y = b//33
b_x = b % 33

for i in range(17,17+16,1):
    for j in range(33):
        if b_y > i-17:
            #w_c
            for k in range(3):
                for l in range(3):
                    ab[i*3+k][j*3+l] = b_c[k][l]
        elif b_y == i-17:
            if b_x > j:
                for k in range(3):
                    for l in range(3):
                        ab[i*3+k][j*3+l] = b_c[k][l]
            else:
                for k in range(3):
                    for l in range(3):
                        ab[i*3+k][j*3+l] = b_o[k][l]
        else:
            for k in range(3):
                for l in range(3):
                    ab[i*3+k][j*3+l] = b_o[k][l]                    

print(99,99)
                    
for i in range(99):
    print(*ab[i],sep="")

