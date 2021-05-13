def out(bnum):
    print(' '+str(bnum['1f']).replace(',','')[1:10*2])
    print(' '+str(bnum['2f']).replace(',','')[1:10*2])
    print(' '+str(bnum['3f']).replace(',','')[1:10*2])
    
n = int(input())
b1 = {'1f': [0]*10, '2f': [0]*10, '3f': [0]*10}
b2 = {'1f': [0]*10, '2f': [0]*10, '3f': [0]*10}
b3 = {'1f': [0]*10, '2f': [0]*10, '3f': [0]*10}
b4 = {'1f': [0]*10, '2f': [0]*10, '3f': [0]*10}
for i in range(n):
    b, f, r, v = map(int,input().split())
    r -= 1
    if b == 1:
        b1[repr(f)+'f'][r] += v
    elif b == 2:
        b2[repr(f)+'f'][r] += v
    elif b == 3:
        b3[repr(f)+'f'][r] += v
    elif b == 4:
        b4[repr(f)+'f'][r] += v
out(b1)
print('#'*20)
out(b2)
print('#'*20)
out(b3)
print('#'*20)
out(b4)