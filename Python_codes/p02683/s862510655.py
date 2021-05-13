import itertools

n,m,x = map(int, input().split())
result_list = [[0 for i in range(m+1)] for i in range(2**n)]
book_list=[]
zero_one = [0,1]
combi_list = list(itertools.product(zero_one, repeat=n))
for i in range(n):
    can = list(map(int, input().split()))
    book_list.append(can)
#2^n通りの組み合わせ
for i in range(2**n):
    #n個全部足す
    for j in range(n):
        #価格とスキルを全部足す
        for k in range(m+1):
            result_list[i][k] +=  book_list[j][k] * combi_list[i][j]
Ans_list = []
for i in range(len(result_list)):
    kari_list = result_list[i][1:]
    if min(kari_list) >= x:
        Ans_list.append(result_list[i][0])
if Ans_list == []:
    print(-1)
else:
    Ans = min(Ans_list)
    print(Ans)