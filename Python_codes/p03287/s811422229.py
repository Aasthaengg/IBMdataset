from itertools import accumulate

def equalfind(A):#配列中の等しい要素の組をカウント　オーダーはO(NlogN)
    A.sort()
    s=1
    count=0
    if len(A)==1:
        return count
    else:
        for i in range(0,len(A)-1):
            if A[i]==A[i+1]:
                s+=1
            else:
                count+=s*(s-1)//2
                s=1
        return count+s*(s-1)//2


N,M=map(int,input().split())
A=list(map(int,input().split()))
A=list(accumulate(A))
X=[A[i]%M for i in range(0,N)]
X.append(0)
print(equalfind(X))