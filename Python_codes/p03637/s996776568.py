input()
l=[int(i)%4 for i in input().split()]
c=l.count
print('YNeos'[c(0)+c(2)//2<len(l)//2::2])