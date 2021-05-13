# for i in range(m):
# for i in range(int(input())):
#n,k= map(int, input().split())
#for _ in range(int(input())):
    #n,k= map(int, input().split())
#from collections import Counter
n=int(input())
if n%360==0:
    print(0)
    exit()
else:
    var=1
    while (var*n)%360!=0:
        var+=1
    print(var)
