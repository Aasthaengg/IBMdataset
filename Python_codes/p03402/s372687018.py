a,b=map(int,input().split())
a-=1
b-=1
l=[['#']*100 for _ in range(20)]+[['.']*100 for _ in range(20)]
for i in range(0,a//50*2,2):
    l[i]=['.','#']*50
for i in range(0,a%50*2,2):
    l[a//50*2][i]='.'
for i in range(21,21+b//50*2,2):
    l[i]=['#','.']*50
for i in range(0,b%50*2,2):
    l[21+b//50*2][i]='#'
print(40,100)
for x in l:
    print(''.join(x))