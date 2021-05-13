n,m,x = map(int,input().split())
books = []

for i in range(n):
    book = list(map(int,input().split()))
    books.append(book)

min_money = -1

#n冊あるとき、2**n通りの選び方
count = 0
for i in range(2**n):
    select = format(count, "0" + str(n) + "b")
    lst = []
    while "1" in select:
        index = select.index("1")
        lst.append(books[index])
        select = select.replace("1","0",1)
    for j in range(1,m+1):
        skill = sum([lst[k][j] for k in range(len(lst))])
        if skill < x:
            break
    else:
        sum_money = sum([lst[j][0] for j in range(len(lst))])
        if min_money != -1:
            min_money = min(min_money, sum_money)
        else:
            min_money = sum_money

    count += 1

print(min_money)