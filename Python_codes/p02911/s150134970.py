n,k,q = map(int,input().split())
a = [int(input()) for i in range(q)]
b = [0 for i in range(n)]

for i in range(q):
    num_ans_person = a[i]-1
    b[num_ans_person] += 1

for i in range(n):
    if k-q+b[i]>0:
        print("Yes")
    else:
        print("No")