
import sys

def enum_div(n):
    ir=int(n**(0.5))+1
    ret=[]
    for i in range(1,ir):
        if n%i == 0:
            ret.append(i)
            if (i!= 1) & (i*i != n):
                ret.append(n//i)
    return ret

from collections import deque    
#    q = deque(l)
#    q.append(4) # 後ろから4を挿入, l=deque([0,1,2,3,4])
#    q.appendleft(5)#前から5を挿入, l=deque([5,0,1,2,3,4])
#    x = q.pop() #後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
#    y = q.popleft() # 前の要素を取り出す, y=5, l = deque([0,1,2,3])

def get_primenumber(number):#エラトステネスの篩
    prime_list = []
#    search_list = deque(list(range(2,number+1)))
    search_list = list(range(2,number+1))
    #search_listの先頭の値が√nの値を超えたら終了
#    while search_list[0] <= math.sqrt(number):
    while search_list[0]**2 <= number:
      #search_listの先頭の値が√nの値を超えたら終了
      #search_listの先頭をprime_listに入れて、先頭をリストに追加して削除
#        head_num = search_list.popleft()
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        #head_numの倍数を除去
#        search_list =deque( [num for num in search_list if num % head_num != 0])
        search_list =[num for num in search_list if num % head_num != 0]
    #prime_listにsearch_listを結合
    prime_list.extend(search_list)
    return prime_list

n=int(input())
ap=list(map(int,input().split()))
amin=min(ap)
amax=max(ap)

if amax==1:
    print("pairwise coprime")
    sys.exit()

if amin!=1:
    bp=enum_div(amin)+[amin]
    bp.sort()
    bp=bp[1:]
    for bpi in bp:
        yn=""
        for ai in ap:
            if ai%bpi!=0:
                yn="coprime"
                break
        if yn=="":
            print("not coprime")
            sys.exit()

if n>=78500 :
    print("setwise coprime")
    sys.exit()

aa=[0]*(amax+1)
for ai in ap:
    aa[ai]+=1

#p=get_primenumber(amax)

#for pp in p:
for pp in range(2,amax+1):
    psum=sum(aa[pp: :pp])
#    print("pp:",pp,psum)
    if psum>=2:
            print("setwise coprime")
            sys.exit()
## max_13.txt ... max_16.txt : "setwise coprime"
print("pairwise coprime")
   
