n,m,l = [int(x) for x in raw_input().split()]

A = []
for idx in range(0,n):
    A.append([int(x) for x in raw_input().split()])

B = []
for idx in range(0,m):
    B.append([int(x) for x in raw_input().split()])

for line in range(0, n):
    result_list = []
    for idx1 in range(0, l):
        sum = 0
        for idx2 in range(0, m):
            sum += A[line][idx2] * B[idx2][idx1]
        result_list.append(sum)
    
    result_str = ""
    for result in result_list:
        result_str += str(result) + " "
    print result_str.rstrip()