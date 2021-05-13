S_list = [(input()) for i in range(2)]
n,m = map(int,S_list[0].split())
S_list_1 = list(map(int,S_list[1].split()))
sum_homework = sum(S_list_1)
if  sum_homework > n:
    result = -1
else:
    result = n - sum_homework
print(result)