num = map(int,raw_input().split())
for x in xrange(0,2):
    for i in xrange(0,2):
        if num[i] > num[i+1] :
            tmp = num[i]
            num[i] = num[i+1]
            num[i+1] = tmp
strnum = map(str,num)
print strnum[0]+" "+strnum[1]+" "+strnum[2]