# coding: utf-8
# Your code here!
N,M=map(int,input().split())
tmp=M*1900+(N-M)*100
cnt=1
for i in range(M):
    cnt*=2
#print(cnt)
print(tmp*cnt)