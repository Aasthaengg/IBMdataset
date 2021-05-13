n=int(input())
d=list(map(int, input().split()))

def mergesort(a):
    def _merge_sort(a, left: int, right: int):
        if left < right:
            center = (left+right)//2

            _merge_sort(a,left,center)
            _merge_sort(a,center+1,right)

            #pは前半部をbuffにコピーする際のインデックス、jで取り出す
            p=j=0
            i=k=left

            #配列の前半部をbuffにコピー
            while i <= center:
                buff[p]=a[i]
                p+=1
                i+=1

            #後半部をコピーされた前半部と比較、小さい方をaに格納していく
            while i<= right and j < p:
                if buff[j] <= a[i]:
                    a[k]=buff[j]
                    j+=1
                else:
                    a[k]=a[i]
                    i+=1
                k+=1

            while j < p:
                a[k] =buff[j]
                k+=1
                j+=1

    n=len(a)
    #merge結果を一時的に格納
    buff=[None]*n
    _merge_sort(a,0,n-1)
    del buff

mergesort(d)
print(d[(n//2)]-d[(n//2)-1])