#B - Guidebook AC(ヒント)
N = int(input())
S = []
P = []
for _ in range(N):
    s,p = input().split()
    S.append(s)
    P.append(int(p)*(-1))#負の値にして降順にソートできるようにする

book = list(zip(S,P))
book_sort = sorted(book)
ans = [book.index(i)+1 for i in book_sort]
for j in ans:
    print(j)