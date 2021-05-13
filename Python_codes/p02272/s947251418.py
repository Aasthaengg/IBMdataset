m=0
def merge(a,left,mid,right):
    n1=mid-left
    n2=right-mid
    el=range(0,n1+1)
    ar=range(0,n2+1)
    for i in range(n1):
        el[i]=a[left+i]
    for i in range(n2):
        ar[i]=a[mid+i]
    el[n1]=float("inf")
    ar[n2]=float("inf")
    i=0
    j=0
    for k in range(left,right):
        global m
        m+=1
        if(el[i] <= ar[j]):
            a[k] = el[i]
            i=i+1
        else:
            a[k]=ar[j]
            j=j+1

def merge_sort(a,left,right):
    if(left+1<right):
        mid=(left+right)//2
        merge_sort(a,left,mid)
        merge_sort(a,mid,right)
        merge(a,left,mid,right)
    else:
        if(a[left]>a[right-1]):
            a[left],a[right-1]=a[right],a[left]



n=int(input())
s=raw_input()
a=list(map(int,s.split()))
merge_sort(a,0,n)
a=map(str,a)
print(" ".join(list(a)))
print(m)