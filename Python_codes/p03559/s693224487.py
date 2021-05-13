N=int(input())

A = map(int,input().split())
B = map(int,input().split())
C = map(int,input().split())

Z = []

for a in A:
    Z.append([a,0])
    
for b in B:
    Z.append([b,1])

for c in C:
    Z.append([c,2])
    
Z.sort()

accum_a = 0
a_buf = 0
accum_c = 0
c_buf = 0
b_buf = 0
prev_z = 0
ans = 0
for z in Z:
    if z[0]==prev_z:
        if z[1]==0:
            a_buf+=1
        elif z[1]==1:
            b_buf+=1
        else:
            c_buf+=1
    else:
        prev_z = z[0]
        accum_c+=c_buf
        ans+=b_buf*(N-accum_c)*accum_a
        accum_a+=a_buf
        a_buf=0
        b_buf=0
        c_buf=0
        if z[1]==0:
            a_buf+=1
        elif z[1]==1:
            b_buf+=1
        else:
            c_buf+=1
            
print(ans)