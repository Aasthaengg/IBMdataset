def is_palindromic(N):
    N_reversed=list(str(N))
    N_reversed.reverse()
    N_reversed=int(''.join(N_reversed))
    if N_reversed==N:
        return True
    else:
        return False
A,B=map(int,input().split())
count=0
for i in range(A,B+1):
    if is_palindromic(i):
        count+=1
print(count)