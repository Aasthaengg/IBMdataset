a,b,k = map(int,input().split())
ans_list = []
for i in range(a,a+k):
    ans_list.append(i)
    if ans_list[-1] == b:
        [print(i) for i in ans_list]
        exit()
for i in range(b-k+1,b+1):
    if ans_list.count(i) == 0:
        ans_list.append(i)
[print(i) for i in ans_list]