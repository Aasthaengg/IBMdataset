A,B=map(int,input().split())

s_list=[['#' for i in range(100)] for j in range(50)] \
            +[['.' for i in range(100)] for j in range(50)]

print(100,100)

n=0
for i in range(A-1):
    if 2*i-100*(n//2)<100:
        s_list[n][2*i-100*(n//2)]='.'
    else:
        n+=2
        s_list[n][2*i-100*(n//2)]='.'

n=52
for i in range(B-1):
    if 2*i-100*((n-52)//2)<100:
        s_list[n][2*i-100*(n-52)//2]='#'
    else:
        n+=2
        s_list[n][2*i-100*(n-52)//2]='#'
for s in s_list:
    print(''.join(s))

