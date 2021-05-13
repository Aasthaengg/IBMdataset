N = int(input())
a = list(map(int,input().split()))

a_abs = [abs(x) for x in a]
abs_max_index = a_abs.index(max(a_abs))
abs_max = a[abs_max_index]
print(2*N)
for i in range(N):
    print('{} {}'.format(abs_max_index+1,i+1))
if abs_max >= 0:
    print('{} {}'.format(abs_max_index+1,1))
    for i in range(1,N):
        print('{} {}'.format(i,i+1))
else:
    print('{} {}'.format(abs_max_index+1,N))
    for i in range(N-1):
        print('{} {}'.format(N-i,N-i-1))