h,w=map(int,input().split())
A=[list(input()) for i in range(h)]
f=['#' for i in range(w+2)]
print(''.join(f))
for i in A:
    print(''.join('#'+(''.join((i)))+'#'))
print(''.join(f))