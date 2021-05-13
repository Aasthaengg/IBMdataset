a,b=map(int,input().split())
ans=[['#' for i in range(100)] for j in range(50)]
ans+=[['.' for i in range(100)] for j in range(50)]
for i in range(a-1):
    ans[(i//50)*2][(i%50)*2]='.'
for i in range(b-1):
    ans[(i//50)*2+52][(i%50)*2]='#'
print(100,100)
for i in range(100):
    print(''.join(ans[i]))
