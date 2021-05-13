n, k=map(int,input().split())
h=[0]*n
for i in range(n):
    h[i]=int(input())

def quicksort(a, left: int, right: int):
    #a[left]〜a[right]をクイックソート
    pl=left
    pr=right
    pivot= a[(left +right)//2]

    #print(f'a[{left}]~a[{right}] : ', *a[left : right +1])

    while pl<=pr:
        while a[pl] <pivot: pl+=1
        while a[pr] >pivot: pr-=1
        if pl <= pr:
            a[pl], a[pr]= a[pr], a[pl]
            pl+=1
            pr-=1

    if left < pr: quicksort(a, left, pr)
    if pl < right: quicksort(a, pl, right)

def quick_sort(a):
    quicksort(a, 0, len(a)-1)
mn=10**9
quick_sort(h)
for i in range(n-k+1):
    dif=h[i+k-1]-h[i]
    if dif<mn:
        mn=dif

print(mn)
