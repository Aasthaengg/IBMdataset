n = int(input())
k = int(input())
x_lst = list(map(int,input().split()))

idoukyori = 0
for x in x_lst:
    idoukyori += 2*min(abs(0-x),abs(k-x))

print(idoukyori)