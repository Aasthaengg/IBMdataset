A,B,K = map(int,input().split())

ans_lst = []
for i in range(1,min(A,B)+1):
    if A%i==0 and B%i==0:
        ans_lst += [i]
ans_lst.reverse()
print(ans_lst[K-1])