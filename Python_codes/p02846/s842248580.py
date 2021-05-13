T = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = T[0]*A[0] + T[1]*A[1]
b = T[0]*B[0] + T[1]*B[1]

if(a==b):
    print("infinity")
    exit()

if(a<b):
    A[0], B[0] = B[0], A[0]
    A[1], B[1] = B[1], A[1]


a = T[0]*A[0] # tak
b = T[0]*B[0] # aok

if a>b:
    print(0)
    exit()

left = 1
right = 10**20

while left+1!=right:
    center = (left+right)//2
    tak = a + (center-1) * (A[0]*T[0]+A[1]*T[1])
    aok = b + (center-1) * (B[0]*T[0]+B[1]*T[1])

    if(tak==aok):
        ans = (center-1)*2
        print(ans)
        exit()
    elif aok<tak:
        right = center
    else:
        left = center

ans = (left-1)*2 + 1
print(ans)