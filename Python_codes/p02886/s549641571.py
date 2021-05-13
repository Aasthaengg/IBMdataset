# https://atcoder.jp/contests/abc143/tasks/abc143_b
n=int(input())
item_list=list(map(int,input().split()))
c=int((n*(n-1))/2)
Answer=0
for i  in range(c):
    for k in range(i+1,n,1):
        Answer+=item_list[i]*item_list[k]

    
print(Answer)