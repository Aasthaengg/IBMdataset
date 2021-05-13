N=int(input())
*A,=map(int,input().split())
s=list(map(lambda x: x//400, A))

mm=len(set([i for i in s if i<8])) 
o=len([i for i in s if 8<=i]) # 色を変えられる人
print(mm if 1<=mm else 1,min(N,mm+o))