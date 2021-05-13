def bingo():
    for i in a:
        tmp=0
        for j in i:
            if j in b:
                tmp+=1
        if tmp==3:
            return True
    for i in range(3):
        tmp=0
        for j in a:
            if j[i] in b:
                tmp+=1
        if tmp==3:
            return True
    tmp=[(a[i][i] in b) for i in range(3)]
    if tmp.count(True)==3:
        return True
    tmp=[a[0][2] in b,a[1][1] in b,a[2][0] in b]
    if tmp.count(True)==3:
        return True

a=[[int(i)for i in input().split()]for j in range(3)]
n=int(input())
b=[int(input())for i in range(n)]
bingo=bingo()
print("Yes" if bingo else "No")