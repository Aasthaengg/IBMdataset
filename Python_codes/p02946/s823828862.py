


def fun(n,num,count):

    if count == (num*2)-1:
        return
    print(n,end=" ")
    count +=1
    fun(n+1,num,count)
xnum=list(map(int,input().split()))
x=xnum[1]
num=xnum[0]

m=x-(num-1)

fun(m,num,0)


