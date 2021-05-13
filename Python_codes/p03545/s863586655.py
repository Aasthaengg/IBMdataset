#C - Train Ticket
A = list(map(int,input()))    

for i in range(1<<3):
    culc = A[0]
    box = []
    for j in range(3):
        mask = 1<<j
        if mask & i != 0:
            culc += A[j+1]
            box.append('+')
        else:
            culc -= A[j+1]
            box.append('-')
    if culc == 7:
        break
ans = [0]*7
ans[::2]=[str(i) for i in A]
ans[1::2]=box
ans.append('=7')
print(''.join(ans))