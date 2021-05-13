a,b=list(map(int,input().split()))

s=[['.' if i<50 else '#' for j in range(100)] for i in range(100)]

a-=1
b-=1

for i in range(1,50,2):
    for j in range(0,100,2):
        if b>0:
            s[i][j]='#'
            b-=1
        if a>0:
            s[i+50][j]='.'
            a-=1
print('100 100')
for i in range(100):
    print(''.join(s[i]))
