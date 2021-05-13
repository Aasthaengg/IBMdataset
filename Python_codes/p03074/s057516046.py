 #ランレングス圧縮とは RLE(Run Length Encoding)とも言われます。
#連続したデータを、ひとつ分のデータと連続した長さで表現します。
def rle(s):
    tmp, count, ans_c,ans_n = int(s[0]),1,[] , []
    for i in range(1,len(s)):
        if tmp == int(s[i]):
            count += 1
        else:
            ans_c.append(tmp)
            ans_n.append(count)
            tmp = int(s[i])
            count = 1
    ans_c.append(tmp)
    ans_n.append(count)
    return ans_c,ans_n

# 初期入力
import sys
input = sys.stdin.readline
N,K = (int(x) for x in input().split())
S =input().strip()

#0と1が何回続くか
a_c,a_n =rle(S)
a_len =len(a_c)
a_n +=[0]
count =[0]*a_len
ans =0

#
if K >= (a_len +1)//2:
    ans =N
elif a_len==2:
    ans =N
elif a_len ==3 and a_c[0]==1:
    ans=N
else:
    if a_c[0] ==1:
        i=2
        indx =i +2*K 
        count[0] =sum(a_n[:0 +2*K +1])
        while not(indx ==a_len+2 or indx ==a_len+1):
            count[i] =count[i-2] -a_n[i-2] -a_n[i-1] + a_n[indx-1] +a_n[indx]
            i +=2
            indx =i +2*K 
    else:
        count[0] =sum(a_n[:2*K])
        count[1] =sum(a_n[1: 1+2*K+1])
        i=3
        indx =i +2*K 
        while not(indx ==a_len+2 or indx ==a_len+1):
            count[i] =count[i-2] -a_n[i-2] -a_n[i-1] + a_n[indx-1] +a_n[indx]
            i +=2      
            indx =i +2*K 
    ans =max(count)
print(ans)