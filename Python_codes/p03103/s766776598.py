from collections import defaultdict
n,m=map(int,input().split())

price_list=[0]*n
num_dic=defaultdict(int)

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

for i in range(n):
    a,b=map(int,input().split())
    price_list[i]=a
    if num_dic[price_list[i]] is None:
        num_dic[price_list[i]]=b
    else:
        num_dic[price_list[i]]+=b

mergesort(price_list)
#同じ値段と違う値段で場合分け
price_sum=0
drink_count=0
for i in range(n):
    if i!=0 and price_list[i-1]==price_list[i]:
        continue
    else:
        #i番目のドリンクを買い占め
        drink_count+=num_dic[price_list[i]]
        if drink_count>m:
            drink_count-=num_dic[price_list[i]]
            stop=i
            break
        p=price_list[i]*num_dic[price_list[i]]
        price_sum+=p

k=m-drink_count
price_sum+=price_list[i]*k

print(price_sum)