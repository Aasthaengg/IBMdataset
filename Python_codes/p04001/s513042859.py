S = input()
lng = len(S) - 1
#print(lng)
cnt = 0

for i in range(2**lng):
    A = format(i, '09b')
    A = A[-lng:]
    #print(A)
    slc = 0
    for j in range(lng):
        #print(j)
        #print(int(A[j]))
        if int(A[j]):
            #print(int(S[slc:j+1]))
            cnt += int(S[slc:j+1])
            #cnt += int(S[slc:j+1])
            slc = j +1
    #print(int(S[slc:]))
    cnt += int(S[slc:])
print(cnt)