# # # coding=utf-8
# # # Author: lee215

get = lambda: int(raw_input().strip())
getl = lambda: raw_input().strip()
gets = lambda: map(int, raw_input().strip().split())
getss = lambda n: [gets() for _ in xrange(n)]

# 2019-03-30 20:14

A, B, C = gets()


# def solve(A, B, C):
#     if len(set([A, B, C])) < 3:
#         print 'Yes'
#     else:
#         print 'No'



def solve(A, B, C):
    if len(set([A, B, C])) == 1:
        print 'Yes'
    else:
        print 'No'

solve(A, B, C)
