A,B,C=map(int,input().split())

modd=A%B
for i in range(B):
    if modd*i%B==C:
        print('YES')
        exit()

print('NO')
