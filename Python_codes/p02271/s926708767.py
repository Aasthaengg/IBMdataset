# get n  list_n
n = int(input())
list_n = [int(x) for x in input().split(' ')]

# get q list_q
q = int(input())
list_q = [int(x) for x in input().split(' ')]

#define recursion find_partial_sum
#input: integer list and M
#output boolean

def find_partial_sum(idx, M):
    if 0 > M or idx >= n:
        return False
    i = list_n[idx]
    if M == i:
        return True
    if find_partial_sum(idx+1, M-i) or find_partial_sum(idx+1, M):
        return True
    return False
#iterate q and check find_åparcial_sum(list_n, q_i) and print
for q_i in list_q:
    if sum(list_n) < q_i:
        print("no")
    elif find_partial_sum(0, q_i):
        print('yes')
    else:
        print('no')
