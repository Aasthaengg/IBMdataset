H, W, A, B = map(int, input().split())

if A > W/2 or B > H/2:
    print('No')
    exit()

for i in range(H):
    if i < B:
        print('0'*(W-A)+'1'*A)
    else:
        print('1'*(W-A)+'0'*A)
