N=int(input())
l =list(map(int,input().split()))
cnt =0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
         if l[i] !=l[j] and l[j] != l[k] and l[k] !=l[i] and max(max(l[i],l[j]) ,l[k]) < l[i]+l[j]+l[k] - max(max(l[i],l[j]) ,l[k]):
             cnt +=1

print(cnt)