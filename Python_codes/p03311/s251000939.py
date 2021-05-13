def total(inlist,k):
    print(sum([ abs(i-k) for i in inlist ]))
    return
n = int(input())
a_list = [ int(v) for v in input().split() ]
a_list = [ v-i for i, v in enumerate(a_list,1) ]
a_list.sort()

total(a_list,a_list[n//2])