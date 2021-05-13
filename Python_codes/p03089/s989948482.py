import sys
sys.setrecursionlimit(1000000)
#def input():
#    return sys.stdin.readline()[:-1]

'''
n=int(input())
for i in range(n):
    a[i]=int(input())
    a[i],b[i]=map(int,input().split())
a=[int(x) for x in input().split()]
n,m=map(int,input.split())
from operator import itemgetter
a = [(1, "c", 1), (1, "b", 3), (2, "a", 0), (1, "a", 2)]
print(sorted(a))  # 0 番目の要素でソート、先頭の要素が同じなら 1 番目以降の要素も見る
print(sorted(a, key=itemgetter(0)))  # 0 番目の要素だけでソート
print(sorted(a, key=itemgetter(0, 2)))  # 0 番目と 2 番目の要素でソート
print(sorted(a, key=lambda x: x[0] * x[2]))  # 0 番目の要素 * 2 番目の要素でソート
print(sorted(a, reverse=True))  # 降順にソート
a.sort()  # 破壊的にソート、sorted() よりも高速
try: # エラーキャッチ list index out of range
    for i in range():
        k=b[i]
except IndexError as e:
    print(i)
'''

test_data1 = '''\
3
1 2 1
'''

test_data2 = '''\
2 3 0
4 5 6
7 8 9
-1 2 -5
'''

test_data3 = '''\
9
1 1 1 2 2 1 2 3 2
'''
td_num=3

def GetTestData(index):
    if index==1:
        return test_data1
    if index==2:
        return test_data2
    if index==3:
        return test_data3

if False:
    with open("../test.txt", mode='w') as f:
        f.write(GetTestData(td_num))
    with open("../test.txt") as f:
        # Start Input code ---------------------------------------
        n=int(f.readline())
        b=list(map(int,f.readline().split()))
        # End Input code ---------------------------------------
else:
    for i in range(1):
        # Start Input code ---------------------------------------
        n=int(input())
        b=list(map(int,input().split()))
        # End Input code ---------------------------------------
#print('n,m,x,y=',n,m,x,y)
ans=[]
#print(b)
cnt=0
while cnt<100 and len(b)>0:
    m=len(b)
    cnt+=1
    flg=False
    for i in range(m):
        #print('i,i+1,m-1-i,b[m-1-i]',i,i+1,m-1-i,b[m-1-i],b)
        if b[m-1-i]==m-i:
            ans.append(b.pop(m-1-i))
            
            flg=True
            break
    if flg==False:
        break
if len(ans)==n:
    for i in range(n):
        print(ans[-i-1])
else:
    print(-1)
